# -*_coding:utf-8-*-

from lemonbook import app
from flask import render_template

@app.route('/')
@app.route('/people/<uid>')
def base(uid=None):
    return render_template('base.html',uid=uid)

@app.route('/about/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/about/app')
def app():
    return render_template('app.html')
