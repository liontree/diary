#!/usr/bin/env python
# -*-coding:utf-8-*-

from lemondiary import app
from flask import render_template, request, flash, redirect, url_for
from lemondiary.models.user_models import User
from lemondiary.forms.userForm import LoginForm, RegisterForm


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
            if user is None:
                flash(u'你的邮箱还没有被注册')
            else:
                #关于密码的存储方式需要更改
                if user.password != password:
                    flash(u'密码不匹配')
                else:
                    return redirect(url_for('base',name=user.username))
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        username = request.form['username'].strip()
        register_result = RegisterForm(email=email, password=password, username=username).checkValid()
        if register_result.is_success is True:
            user = User().query_by_email(email)
            if user is None:
                User().addAccount(email=email, password=password, username=username)
                return redirect(url_for('base',name=username))
            else:
                flash(u"该邮箱已经被注册")
                return redirect(url_for('register'))
        else:
            return redirect(url_for('register'))
    else:
        return redirect(url_for('register'))
