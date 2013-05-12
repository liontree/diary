#!/usr/bin/env python
# -*-coding:utf-8-*-

from flask.ext.sqlalchemy import SQLAlchemy
from lemonbook import app

db = SQLAlchemy(app)
def create_app():
    db.init_app(app)
    return app

'''
http://pythonhosted.org/Flask-SQLAlchemy/quickstart.html

Road to Enlightenment
The only things you need to know compared to plain SQLAlchemy are:

    SQLAlchemy gives you access to the following things:
    all the functions and classes from sqlalchemy and sqlalchemy.orm
    a preconfigured scoped session called session
    the metadata
    the engine
    a SQLAlchemy.create_all() and SQLAlchemy.drop_all() methods to create and drop tables according to the models.
    a Model baseclass that is a configured declarative base.
    The Model declarative base class behaves like a regular Python class but has a query attribute attached that can be used to query the model. (Model and BaseQuery)
    You have to commit the session, but you don’t have to remove it at the end of the request, Flask-SQLAlchemy does that for you.



init_app(app)
This callback can be used to initialize an application for the use with this database setup. Never use a database in the context of an application not initialized that way or connections will leak.
'''
