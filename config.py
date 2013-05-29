#!/usr/bin/env python

DEBUG=True
SQLALCHEMY_DATABASE_URI = ''
SECRET_KEY=''
PORT=''
HOST=''

MAIL_HOST=''
MAIL_USERNAME=''
MAIL_PASSWORD=''

#import local_config
try:
    from lemonbook.local_config import *
except:
    pass
'''
http://pythonhosted.org/Flask-SQLAlchemy/config.html

Connection URI Format
For a complete list of connection URIs head over to the SQLAlchemy documentation under (Supported Databases). This here shows some common connection strings.

SQLAlchemy indicates the source of an Engine as a URI combined with optional keyword arguments to specify options for the Engine. The form of the URI is:

    dialect+driver://username:password@host:port/database
    Many of the parts in the string are optional. If no driver is specified the default one is selected (make sure to not include the + in that case).

    Postgres:

    postgresql://scott:tiger@localhost/mydatabase
    MySQL:

    mysql://scott:tiger@localhost/mydatabase
    Oracle:

    oracle://scott:tiger@127.0.0.1:1521/sidname
    SQLite (note the four leading slashes):

    sqlite:////absolute/path/to/foo.db
'''
