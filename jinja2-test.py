#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)

@app.route('/')
def jinja_test():
    return render_template('jinja2.html', title='jinja2')

@app.route('/about')
def about():
    return 'about'

if __name__ == '__main__':
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)