#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask_bootstrap import Bootstrap
from flask import Flask, render_template,request
from livereload import Server
from flask_nav import Nav
from flask_nav.elements import *

app = Flask(__name__)
# 注册bootstrap
bootstrap = Bootstrap(app)

nav = Nav()

@nav.navigation()
def top():
    return Navbar(
        u'Imperio',
         View(u'首页','about'),View(u'关于','about'),
        View(u'服务','about'),View(u'标签','about'),
    )

nav.init_app(app)

@app.route('/')
def flask_bootstrap_test():
    return render_template('bootstrap-test.html', title='bootstrap_test')

@app.route('/about')
def about():
    return 'about'

if __name__ == '__main__':
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=False)