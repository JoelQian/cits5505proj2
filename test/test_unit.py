import os
os.environ['TESTING'] = 'TRUE'

import unittest
from app import app, db   
from app.models import User  
class TestAuth(unittest.TestCase):

    def setUp(self):

        self.app = app.test_client()
        with app.app_context():
            db.create_all()
            db.session.query(User).delete()

    def tearDown(self):

        with app.app_context():
            db.session.remove()  
            db.session.rollback()  
            db.engine.dispose()

    def test_register(self):
        
        response = self.app.post('/register', data=dict(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        ))
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 200)
        self.assertEqual(data['message'], 'User registered successfully!')

    def test_login(self):
        
        with app.app_context():
            self.app.post('/register', data=dict(
                username='testuser',
                email='test@example.com',
                password='testpassword'
            ))
        
        response = self.app.post('/login', data=dict(
            username='testuser',
            password='testpassword'
        ))
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 200)
        self.assertEqual(data['message'], 'Login successful!')


    def test_new_discussion_get(self):
            # Ensure no user is logged in by clearing cookies
            self.app.get('/logout')
            
            # Access the new discussion page with GET
            response = self.app.get('/new-discussion')
            
            # Check if the response is JSON
            self.assertEqual(response.content_type, 'application/json')
            
            data = response.get_json()
            
            # Check if the user is prompted to log in
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['code'], 201)
            self.assertEqual(data['message'], 'Please login first!')

    def test_new_discussion_post(self):
        # Simulate user login
        with app.app_context():
            self.app.post('/register', data=dict(
                username='testuser',
                email='test@example.com',
                password='testpassword'
            ))
            self.app.post('/login', data=dict(
                username='testuser',
                password='testpassword'
            ))
        
        # Create a new discussion with POST
        response = self.app.post('/new-discussion', data=dict(
            category_id=1,
            title='Test Title',
            body='Test Body'
        ))
        data = response.get_json()
        
        # Check if the post creation is successful
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 200)
        self.assertIn('post_id', data)

    def test_post_details_post(self):
        # Simulate user login
        with app.app_context():
            self.app.post('/register', data=dict(
                username='testuser',
                email='test@example.com',
                password='testpassword'
            ))
            self.app.post('/login', data=dict(
                username='testuser',
                password='testpassword'
            ))
        
        # Post a comment to the post details page
        response = self.app.post('/post-details/1', data=dict(
            body='Test Comment'
        ))  # assuming post_id 1 exists
        
        data = response.get_json()
        
        # Check if the comment creation is successful
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 200)
        self.assertIn('comment_id', data)

    

if __name__ == '__main__':
    unittest.main()
