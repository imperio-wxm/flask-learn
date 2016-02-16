#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask_bootstrap import Bootstrap
from flask import Flask, render_template,request
from livereload import Server

app = Flask(__name__)
# 注册bootstrap
bootstrap = Bootstrap(app)

@app.route('/',methods=['POST','GET'])
def flask_bootstrap_test():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return username,password
    return render_template('bootstrap_test.html',title='bootstrap_test',methods=request.method)

@app.route('/about')
def about():
    return 'about'

if __name__ == '__main__':
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=False)