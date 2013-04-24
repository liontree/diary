#!/usr/bin/env python
# -*_coding:utf-8-*-

from diary import app
@app.route('/index')
def hello():
    return "hello flask"

if __name__ == '__main__':
    app.run()
