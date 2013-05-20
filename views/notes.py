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

@app.route('/note/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('edit.html')
    elif request.method == 'POST':
        contents = request.form['contents'].strip()
        post_result = EditForm(contents=contents).checkSubmit()
        if post_result.is_success is True:
            user_id = get_user_id()
            Note.addNote(user_id=user_id, contents=contents)
            return "hello"
        else:
            flash("提交内容不能为空")
            return redirect(url_for('create'))
    else:
        return redirect(url_for('create'))

#@app.route('/note/<note_id>')
#def displayall():
#    if request.method == 'GET':
#        return render_template('note.html')
