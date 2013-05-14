# -*-coding:utf-8-*-

from lemonbook import app
from flask import render_template, request, flash, redirect
from lemonbook.models.note_models import Note
from lemonbook.forms.noteForm import EditForm
from flask.ext.login import login_required

#@app.route('/<name>/notes')
#def display_all_notes(name=None):

@app.route('/note/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('edit.html')
    elif request.method == 'POST':
        contents = request.form['contents'].strip()
        submit_result = EditForm(contents=contents).checkSubmit()
        if submit_result.is_success == True:
            #怎么获取userid ?
            note = Note().addNote(user_id=user_id, contents=contents)
            #返回note主页面
            return redirect(url_for('/'))
        else:
            return redirect(url_for('/note/create'))
    else:
        return redirect(url_for('/note/create'))
