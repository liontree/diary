# -*-coding:utf-8-*-

from lemondiary import app
from flask import render_template, request, flash, redirect
from lemondiary.models.note_models import Note
from lemondiary.models.user_models import User

@app.route('/<name>/notes')
def display_all_notes(name=None):
    return render_template('note.html', name=name)
