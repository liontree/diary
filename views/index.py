# -*_coding:utf-8-*-

from lemonbook import app
from flask import render_template

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/about/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/about/app')
def app():
    return render_template('app.html')
