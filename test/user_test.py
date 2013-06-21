# -*-coding:utf-8-*-

import unittest
from lemonbook import app
from lemonbook.extensions import db
from lemonbook.views.user import *
from lemonbook.views.notes import *
from user_test_config import *
from lemonbook.forms.userForm import LoginForm, RegisterForm
from lemonbook.models.user_models import User
from lemonbook.common.secure import securepw,checkpassword

class UserTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def login(self, email, password):
        return self.app.post('/login', data=dict(
            email = email,
            password = password
            ), follow_redirects=True)
        
    def register(self, email, password, username):
        return self.app.post('/register', data=dict(
            email = email,
            password = password,
            username = username
            ), follow_redirects=True)

    def reset(self,email,password):
        return self.app.post('reset', data=dict(
            email = email,
            password = password
            ), follow_redirects=True)

    def test_login(self):
        login_r = LoginForm(email=EMAIL_R, password=PASSWORD_R).checkValid()
        self.assertTrue(login_r.is_success)
        user = User.query_by_email(EMAIL_R)
        self.assertIsNotNone(user)
        check_password = checkpassword(EMAIL_W,EMAIL_R)
        self.assertFalse(check_password)
        rv = self.login(EMAIL_R,PASSWORD_W)
        assert "password does not match" in rv.data
        login_w = LoginForm(email=EMAIL_W, password=PASSWORD_W).checkValid()
        self.assertTrue(login_r.is_success)
        user = User.query_by_email(EMAIL_W)
        self.assertIsNone(user)
        rv = self.login(EMAIL_W,PASSWORD_W)
        assert "Your email has not been registered" in rv.data

    def test_register(self):
        register_r = RegisterForm(email=EMAIL_R, password=PASSWORD_R, username=USERNAME_NEW).checkValid()
        self.assertTrue(register_r.is_success)
        user = User.query_by_email(EMAIL_R)
        self.assertIsNotNone(user)
        rv = self.register(EMAIL_R, PASSWORD_R, USERNAME_NEW)
        assert "The email has already been registered" in rv.data
        user = User.query_by_email(EMAIL_NEW)
        self.assertIsNone(user)
        User.addAccount(email=EMAIL_NEW, password=PASSWORD_NEW, username=USERNAME_NEW)

    def test_reset(self):
        rv = self.reset(EMAIL_W,"111111")
        assert "The email does not exist" in rv.data
        user = User.query_by_email(email=EMAIL_W)
        self.assertIsNone(user)
        rv = self.reset(EMAIL_R,'')
        assert "Please input the new password" in rv.data

if __name__ == '__main__':
    unittest.main()
