# -*-coding:utf-8-*-

import unittest
from lemonbook import app
from lemonbook.views.user import *
from lemonbook.views.notes import *
from user_test_config import *
from lemonbook.forms.userForm import LoginForm, RegisterForm
from lemonbook.models.user_models import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testlogin(self):
        login_r = LoginForm(email=EMAIL_R, password=PASSWORD_R).checkValid()
        self.assertTrue(login_r.is_success)
        user = User.query_by_email(EMAIL_R)
        self.assertIsNotNone(user)

if __name__ == '__main__':
    unittest.main()
