# -*-coding:utf-8-*-


from lemonbook.extensions import db
from lemonbook.common.flask_login import UserMixin, AnonymousUser


class User(db.Model, UserMixin):
    __tablename__ = 'account'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    email = db.Column('email', db.String(64), nullable=False )
    password = db.Column('password', db.String(16), nullable=False)
    username = db.Column('username', db.String(16), nullable=False)
    status = db.Column('status',db.CHAR(1), nullable=False)
    displayid = db.Column('displayid',db.String(16), nullable=True)
    

    def __init__(self,email,password,username,status=True,displayid=None):
        self.email = email
        self.password = password
        self.username = username
        self.status = status
        self.displayid = displayid

    def __repr__(self):
        return '<User %r>' %self.email

    def is_active(self):
        return True
    
    @classmethod
    def query_by_email(cls, email):
        user = User.query.filter_by(email=email).first()
        return user

    
    @classmethod
    def query_by_id(cls, id):
        user = User.query.filter_by(id=id).first()
        return user

    @classmethod
    def query_by_displayid(cls, displayid):
        user = User.query.filter_by(displayid=displayid).first()
        if user is None:
            return True
        else:
            return False

    @classmethod
    def addAccount(cls, email, password, username,status='', displayid=None):
        newpeople = User(email=email, password=password, username=username, status=status, displayid=displayid)
        db.session.add(newpeople)
        db.session.commit()

class Anonymous(AnonymousUser):
    name = u"Anonymous"
