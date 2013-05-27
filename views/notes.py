# -*-coding:utf-8-*-

from lemonbook import app
from flask import render_template, request, flash, redirect, url_for, session
from lemonbook.models.note_models import Note
from lemonbook.models.user_models import User
from lemonbook.forms.noteForm import EditForm
from lemonbook.functionlib.flask_login import login_required


def get_user_id():
    if session.has_key('user_id'):
        return session['user_id']
    return 0


@app.route('/note/<uid>')
@login_required
def display(uid):
    user_id = get_user_id()
    user = User.query_by_id(id=user_id)
    if user.displayid != '':
        uid = user.displayid
    else:
        uid = user.id
    return render_template('note.html',uid=uid)


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('edit.html')
    elif request.method == 'POST' and 'contents' in request.form:
        contents = request.form['contents'].strip()
        if contents == '':
            flash(u"提交内容不能为空")
            return redirect(url_for('create'))
        else:
            user_id = get_user_id()
            user = User.query_by_id(id=user_id)
            Note.addNote(user_id=user_id, contents=contents)
            return redirect(url_for('display',name=user.username))
    else:
        return redirect(url_for('create'))
