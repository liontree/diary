#!/usr/bin/env python
# -*-coding:utf-8-*-

from diary import app
from flask import render_template, request
from diary.models.user_models import User

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        user = User().query_by_email(email)
        if user is None:
            return "Your email has not been registered"
        else:
            if user.password == password:
                return "e...."

