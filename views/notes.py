# -*-coding:utf-8-*-

from lemonbook import app
from flask import render_template, request, flash, redirect
from lemonbook.models.note_models import Note
from lemonbook.models.user_models import User

#@app.route('/<name>/notes')
#def display_all_notes(name=None):
    
