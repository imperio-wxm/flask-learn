#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask import Flask,render_template
from livereload import Server
from flask_wtf_form import loginForm

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def loginTest():
    return

if __name__ == '__main__':
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=False)