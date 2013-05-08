#!/usr/bin/env python
# -*_coding:utf-8-*-

from diary import app
from flask import render_template, flash

@app.route('/')
@app.route('/people/<name>')
def index(name=None):
    return render_template('index.html',name=name)
