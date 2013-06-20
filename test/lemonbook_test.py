import os
import tempfile
import unittest
from lemonbook import app
from lemonbook.models.user_models import *
from lemonbook.models.note_models import *
from lemonbook.extensions import db

from lemonbook.common.secure import *
from test_config import *

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.user = User(EMAIL,PASSWORD,USERNAME,STATUS,DISPLAYID_E)
        self.note = Note(USER_ID, CONTENT)
        db.session.add(self.user)
        db.session.add(self.note)
        db.session.commit()

    def tearDown(self):
        db.session.delete(self.user)
        db.session.delete(self.note)
        db.session.commit()

    def test_query_by_email(self):
        self.assertFalse(User.query_by_displayid(DISPLAYID_NE))
        self.assertTrue(User.query_by_displayid("hehe"))
        user = User.query_by_email(EMAIL)
        self.assertIsInstance(user, User)

    def test_query_by_id(self):
        user = User.query_by_id(self.user.id)
        self.assertIsInstance(user, User)
        self.assertEqual(user, self.user)

    def test_display_latest(self):
        note = Note.display_latest(USER_ID)
        self.assertIsInstance(note, Note)

class ModelAddTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True

    def tearDown(self):
        self.user = User.query.filter_by(email=EMAIL).first()
        db.session.delete(self.user)
        db.session.commit()
    
    def test_add_user(self):
        User.addAccount(EMAIL,PASSWORD,USERNAME,STATUS,DISPLAYID_E)
        user = User.query.filter_by(email=EMAIL).first()
        self.assertIsNotNone(user)

class CommonTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def testDown(self):
        pass

    def test_secure(self):
        sec = securepw(PASSWORD)
        self.assertEqual(len(sec),32)
    
    import hashlib
    def test_checkpassword(self):
        password = "123456"
        sec1 = hashlib.md5(password).hexdigest()
        sec2 = hashlib.md5(PASSWORD).hexdigest()
        self.assertEqual(sec1,sec2)
        self.assertTrue(checkpassword(password,sec2))

'''
class userTest(unittest.TestCase):
    def setUp(self):
        #self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        
    def tearDown(self):
        pass

    def login(self, email, password):
        return self.app.post('/login',data=dict(
            email = email,
            password = password
            ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    #def test_login_logout(self):
        
            #rv : <class 'flask.wrappers.Response'>
        
        #rv = self.login(EMAIL_LOCAL, PASSWORD_LOCAL)

'''



if __name__ == '__main__':
    unittest.main()
