# -*-coding:utf-8-*-


from lemonbook.extensions import db
from lemonbook.functionlib.flask_login import UserMixin, AnonymousUser


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
        return self.status
    
    @classmethod
    def query_by_email(self,email):
        user = User.query.filter_by(email=email).first()
        return user

    
    @classmethod
    def query_by_id(self, id):
        user = User.query.filter_by(id=id).first()
        return user

    #displayid的设定
    def addAccount(self, email, password, username, displayid=None):
        newpeople = User(email=email, password=password, username=username, displayid=displayid)
        db.session.add(newpeople)
        db.session.commit()

class Anonymous(AnonymousUser):
    name = u"Anonymous"
