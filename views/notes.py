# -*-coding:utf-8-*-

import os
from werkzeug import secure_filename
from lemonbook import app
from flask import render_template, request, flash, redirect, url_for, session
from lemonbook.models.note_models import Note
from lemonbook.models.user_models import User
from lemonbook.forms.noteForm import EditForm
from lemonbook.common.flask_login import login_required,current_user
from datetime import datetime
from lemonbook.config import UPLOAD_FOLDER,ALLOWED_EXTENSIONS

def get_user_id():
    if session.has_key('user_id'):
        return session['user_id']
    return 0

def allowed_file(filename):
    return '.' in filename and \
            filename.split('.')[1] in ALLOWED_EXTENSIONS
 

@app.route('/<id>/<date>')
@login_required
def date(id,date):
    user_id = get_user_id()
    notes = Note.query_by_date(user_id=user_id, date=date)
    if notes is None:
        contents = None
    else:
        contents = {}
        for i in range(len(notes)):
            #contents.append(notes[i].contents)
            contents[notes[i].create_time]=notes[i].contents
        print contents
    return render_template('date.html',contents=contents)

@app.route('/latest', methods=['GET','POST'])
@login_required
def latest():
    user_id = get_user_id()
    if request.method == 'GET':
        note = Note.display_latest(user_id=user_id)
        if note is None:
            contents = None
        else:
            contents = note.contents
        return render_template('latest.html',contents=contents)
    elif request.method == 'POST':
        date = request.form['date'].strip()
        date = date.replace('/','')
        return redirect(url_for('date', id=user_id,date=date))

@app.route('/note/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('edit.html')
    elif request.method == 'POST' and 'contents' in request.form:
        contents = request.form['contents'].strip()
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if contents == '':
            flash(u"提交内容不能为空")
            return redirect(url_for('create'))
        else:
            user_id = get_user_id()
            user = User.query_by_id(id=user_id)
            date = datetime.now().strftime('%m%d%Y')
            Note.addNote(user_id=user_id, contents=contents, date=date)
            note = Note.display_latest(user_id=user_id)
            return render_template('post.html',contents=note.contents)
    else:
        return redirect(url_for('create'))
