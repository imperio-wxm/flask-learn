#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask_bootstrap import Bootstrap
from flask import Flask, template_rendered
from livereload import Server

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def flask_bootstrap_test():
    return template_rendered('flask_bootstrap_test.html',title='bootstrap_test')

if __name__ == '__main__':
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=False)