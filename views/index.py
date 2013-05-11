#!/usr/bin/env python
# -*_coding:utf-8-*-

from lemondiary import app
from flask import render_template, flash

@app.route('/')
@app.route('/people/<name>')
def base(name=None):
    return render_template('base.html',name=name)

@app.route('/about/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/404')
def notfound():
    return render_template('404.html')
