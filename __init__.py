# -*- coding:utf-8 -*-

from flask import Flask
from lemonbook.functionlib.flask_login import LoginManager

# --create app--
app = Flask(__name__)
app.config.from_object('lemonbook.config')

loginmanager = LoginManager()

loginmanager.setup_app(app)

import views
