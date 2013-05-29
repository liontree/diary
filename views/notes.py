# -*-coding:utf-8-*-

from lemonbook import app
from flask import render_template, request, flash, redirect, url_for, session
from lemonbook.models.note_models import Note
from lemonbook.models.user_models import User
from lemonbook.forms.noteForm import EditForm
from lemonbook.common.flask_login import login_required,current_user


def get_user_id():
    if session.has_key('user_id'):
        return session['user_id']
    return 0


@app.route('/latest')
@login_required
def latest():
    user_id = get_user_id()
    note = Note.display_latest(user_id=user_id)
    if note is None:
        contents = None
    else:
        contents = note.contents
    return render_template('latest.html',contents=contents)

@app.route('/note/create', methods=['GET', 'POST'])
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
            note = Note.display_latest(user_id=user_id)
            return render_template('post.html',contents=note.contents)
    else:
        return redirect(url_for('create'))
