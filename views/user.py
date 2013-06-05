# -*-coding:utf-8-*-

from lemonbook import app
from flask import render_template, request, flash, redirect, url_for
from lemonbook.models.user_models import User
from lemonbook.models.note_models import Note
from lemonbook.forms.userForm import LoginForm, RegisterForm
from lemonbook.common.flask_login import LoginManager,current_user,login_required,login_user,logout_user,confirm_login,fresh_login_required
from lemonbook.common.secure import securepw,checkpassword
from lemonbook.common.sendmail import *
from notes import get_user_id
from lemonbook.config import MAIL_USERNAME
from threading import Thread

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        login_result = LoginForm(email=email, password=password).checkValid()
        if login_result.is_success is True:
            user = User.query_by_email(email)
            if user is None:
                flash(u'你的邮箱还没有被注册')
                return redirect(url_for('login'))
            else:
                if not checkpassword(password,user.password):
                    flash(u'密码不匹配')
                    return redirect(url_for('login'))
                else:
                    remember = request.form.get("remember", "no") == "yes"
                    login_user(user=user,remember=remember)
                    return redirect(url_for('latest'))
                        
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        username = request.form['username'].strip()
        displayid = request.form['displayid'].strip()
        register_result = RegisterForm(email=email, password=password, username=username).checkValid()
        if register_result.is_success is True:
            user = User.query_by_email(email)
            password = securepw(password)
            if user is None:
                if displayid == '':
                    User.addAccount(email=email, password=password, username=username)
                    Thread(target=send_mail, args=(MAIL_USERNAME,email,"Thanks for registering",success_msg%username)).start()
                elif User.query_by_displayid(displayid=displayid) is True:
                    User.addAccount(email=email, password=password, username=username, displayid=displayid)
                    Thread(target=send_mail, args=(MAIL_USERNAME,email,"Thanks for registering",success_msg%username)).start()
                else:
                    flash(u"已经有人抢先注册此ID了")
                    return redirect(url_for('register'))
                domail = email.split('@')[1]
                if domail == "gmail.com":
                    domail = "http://mail.google.com/"
                else:
                    domail = "http://mail."+email.split('@')[1]+"/"
                return render_template('confirm.html',domail=domail)
            else:
                flash(u"该邮箱已经被注册")
                return redirect(url_for('register'))
        else:
            return redirect(url_for('register'))
    else:
        return redirect(url_for('register'))

@app.route('/findpw',methods=['GET','POST'])
def findpw():
    if request.method == 'GET':
        return render_template('findpw.html')
    elif request.method == 'POST' and 'email' in request.form:
        email = request.form['email'].strip()
        if email == '':
            flash(u"请输入邮箱")
            return redirect(url_for('findpw'))
        else:
            user = User.query_by_email(email=email)
            if user is None:
                flash(u'该邮箱没有被注册')
                return redirect(url_for('findpw'))
            else:
                Thread(target=send_mail, args=(MAIL_USERNAME,email,"find password",pw_msg%(user.username,user.password))).start()
                return render_template('confirm.html',email=email)
    else:
        return render_template('findpw.html')

@app.route('/reset', methods=['GET','POST'])
def reset():
    if request.method == 'GET':
        return render_template('reset.html')
    elif request.method == 'POST' and 'password' in request.form:
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        user = User.query_by_email(email=email)
        if user is None:
            flash(u"该邮箱不存在啊啊啊")
            return redirect(url_for('reset'))
        else:
            if password == '':
                flash(u"请输入新密码")
                return redirect(url_for('reset'))
            else:
                password = securepw(password)
                User.changepw(email=email, password=password)
                return redirect(url_for('login'))
    else:
        return redirect(url_for('reset'))

@app.route('/settings', methods=['GET','POST'])
@login_required
def setting():
    if request.method == 'GET':
        return render_template('settings.html')
    elif request.method == 'POST':
        password_old = request.form['password_old'].strip()
        password_new = request.form['password_new'].strip()
        username_new = request.form['username_new'].strip()
        if password_old and password_new or username_new:
            pass
        if not checkpassword(password_old,current_user.password):
            flash(u'请重新输入原始密码')
            return redirect(url_for('setting'))
        else:
            password_new = securepw(password_new)
            User.changepw(email=current_user.email, password=password_new)
            User.changeusername(email=current_user.email, username=username_new)
            return redirect(url_for('login'))
    else:
        return render_template('settings.html')
