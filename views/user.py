#!/usr/bin/env python
# -*-coding:utf-8-*-

from lemondiary import app
from flask import render_template, request, flash, redirect, url_for
from lemondiary.models.user_models import User
from lemondiary.forms.loginform import LoginForm


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    elif request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        login_result = LoginForm(email=email, password=password).checkValid()
        if login_result.is_success is True:
            user = User().query_by_email(email)
            if user is None:
                #此处模板中还没有完成
                flash(u'Your email has not been registered.')
            else:
                if user.password != password:
                    flash(u'password does not match')
                else:
                    return redirect(url_for('base',name=user.username))
        else:
            return redirect(url_for('signin'))
    else:
        return redirect(url_for('signin'))

@app.route('/logout')
def logout():
    return render_template('base.html')
