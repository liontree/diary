# -*- coding:utf-8 -*-

from flask import Flask

# --create app--
app = Flask(__name__)
app.config.from_object('lemonbook.config')


import views
