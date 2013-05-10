#!/usr/bin/env python
# -*_coding:utf-8-*-

from lemondiary import app
from flask import render_template, flash

@app.route('/')
@app.route('/people/<name>')
def base(name=None):
    return render_template('base.html',name=name)
