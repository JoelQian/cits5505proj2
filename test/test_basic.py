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

if __name__ == '__main__':
    unittest.main()
