# -*-coding:utf-8-*-

from lemonbook import app
from flask import render_template, request, flash, redirect, url_for
from lemonbook.models.note_models import Note
from lemonbook.models.user_models import User
from lemonbook.forms.noteForm import EditForm
from lemonbook.functionlib.flask_login import login_required, get_user_id
#@app.route('/<name>/notes')
#def display_all_notes(name=None):


@app.route('/note/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('edit.html')
    elif request.method == 'POST' and 'contents' in request.form:
        contents = request.form['contents'].strip()
        user_id = get_user_id()
        Note.addNote(user_id=user_id, contents=contents)
        return redirect(url_for('aboutme'))
    else:
        return redirect(url_for('create'))

@app.route('/note/<note_id>')
def displayall():
    if request.method == 'GET':
        return render_template('note.html')
