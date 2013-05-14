#!/usr/bin/env NotImplementedError("No `id` attribute - override get_id"python
# -*-coding:utf-8-*-

from lemonbook.initdb import db, create_app

class UserRight(object):
    '''
    This provides default implementations for the methods that Flask-Login
    expects user objects to have.
    '''
    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)
        except AttributeError:
            raise NotImplementedError("No `id` attribute - override get_id")

class UserWrong(object):
    '''
    This is the default object for other user
    '''
    def is_authenticated(self):
        return False
    
    def is_active(self):
        return False
    
    def is_anonymous(self):
        return True
    
    def get_id(self):
        return None

class User(db.Model, UserRight):
    __tablename__ = 'account'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    email = db.Column('email', db.String(64), nullable=False )
    password = db.Column('password', db.String(16), nullable=False)
    username = db.Column('username', db.String(16), nullable=False)
    status = db.Column('status',db.CHAR(1), nullable=False)
    displayid = db.Column('displayid',db.String(16), nullable=True)
    
    def __inti__(self,email,password,username, status=True, displayid=None):
        self.email = email
        self.password = password
        self.username = username
        self.status = status
        self.displayid = displayid

    def __repr__(self):
        return '<User %r>' %self.email
    
    def is_active(self):
        return self.status

    def query_by_email(self,email):
        user = User.query.filter_by(email=email).first()
        return user
    
    def query_by_id(self, id):
        user = User.query.filter_by(id=id).first()

    #displayid的设定
    def addAccount(self, email, password, username, displayid=None):
        newpeople = User(email=email, password=password, username=username, displayid=displayid)
        db.session.add(newpeople)
        db.session.commit()

class OtherUser(UserWrong):
    username = u"otheruser"

