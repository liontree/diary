# -*_coding:utf-8-*-

from lemonbook import app
from flask import render_template

@app.route('/')
@app.route('/<uid>')
def base(uid=None,contents=None):
    return render_template('base.html',uid=uid,contents=contents)

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/app')
def app():
    return render_template('app.html')
