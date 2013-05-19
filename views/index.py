# -*_coding:utf-8-*-

from lemonbook import app
from flask import render_template

@app.route('/')
@app.route('/people/<name>') #url地址避免出现中文，这个地方是不是显示uid比较好
def base(name=None):
    return render_template('base.html',name=name)

@app.route('/about/aboutme')
def aboutme():
    return render_template('aboutme.html')


