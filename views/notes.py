# -*-coding:utf-8-*-

from lemondiary import app
from flask import render_template, request, flash, redirect


@app.route('/people/<name>/notes')
def display_all_notes(name=None):
    return render_template('default.html')
