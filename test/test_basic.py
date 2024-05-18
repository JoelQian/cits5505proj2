import unittest
from app import app, db   # 假设你的 Flask 应用的模块名为 app
from app.models import User  # 假设你有一个名为 User 的模型

class TestAuth(unittest.TestCase):

    def setUp(self):
        # 创建一个测试客户端
        self.app = app.test_client()
        # 在测试之前设置数据库
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # 使用内存数据库
        with app.app_context():
            db.create_all()
            # 清空现有用户
            db.session.query(User).delete()

    def tearDown(self):
        # 在测试完成后清理数据库
        with app.app_context():
            db.session.remove()  # 移除会话
            db.session.rollback()  # 回滚会话更改
            db.get_engine(app).dispose()  # 关闭数据库连接

    def test_register(self):
        # 发送 POST 请求来测试注册功能
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
        # 先注册一个用户
        with app.app_context():
            self.app.post('/register', data=dict(
                username='testuser',
                email='test@example.com',
                password='testpassword'
            ))
        # 发送 POST 请求来测试登录功能
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
