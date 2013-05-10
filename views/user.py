#!/usr/bin/env python
# -*-coding:utf-8-*-

from lemondiary import app
from flask import render_template, request, flash, redirect, url_for
from lemondiary.models.user_models import User
from lemondiary.forms.loginform import LoginForm


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
                #flash功能模板中还没有完成
                flash(u'Your email has not been registered.')
            else:
                #关于密码的存储方式需要更改
                if user.password != password:
                    flash(u'password does not match')
                else:
                    return redirect(url_for('base',name=user.username))
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    return render_template('base.html')

#@app.route('/register', method=['GET', 'POST'])
@app.route('/register')
def register():
    return render_template('register.html')
    '''
    if request.method == 'GET':
        return render.template('register.html')
    elif request.method == 'POST':
        email = request.form['email'].strip()
        password == request.form['password'].strip()
        username = request.form['username'].strip()
        #验证输入是否符合要求
        #if 符合要求:
            #向表中插入数据
            #return redirect(url_for(欢迎界面))
        else:
            return redirect(url_for('register'))
    else:
        return redirect(url_for('register'))'''
