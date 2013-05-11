#!/usr/bin/env python
# -*-coding:utf-8-*-

from lemondiary.initdb import db, create_app

class User(db.Model):
    __tablename__ = 'account'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    email = db.Column('email', db.String(64), nullable=False )
    password = db.Column('password', db.String(16), nullable=False)
    username = db.Column('username', db.String(16), nullable=False)
    
    def __inti__(self,email,password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' %self.email

    def query_by_email(self,email):
        user = User.query.filter_by(email=email).first()
        return user
    
    def addAccount(self, email, password, username):
        newpeople = User(email=email, password=password, username=username)
        db.session.add(newpeople)
        db.session.commit()
