#!/usr/bin/env python
# -*-coding:utf-8-*-

from diary import app
from flask import render_template, request, flash, redirect
from diary.models.user_models import User
from diary.forms.loginform import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        login_result = LoginForm(email=email, password=password).checkValid()
        if login_result.is_success is True:
            user = User().query_by_email(email)
            if user.email is None:
                flash(u'Your email has not been registered.')
            else:
                if user.password != password:
                    flash(u'password does not match')
                else:
                    return redirect(url_for('index'))
        else:
            flash(login_result.info)
    else:
        return redirect(url_for('login'))
