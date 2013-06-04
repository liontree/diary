import unittest
from lemonbook import app
from lemonbook.models.user_models import *
from lemonbook.models.note_models import *
from lemonbook.extensions import db

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

if __name__ == '__main__':
    unittest.main()
