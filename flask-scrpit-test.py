#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'wxmimperio'

from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)

manager = Manager(app)

@app.route('/init')
@app.route('/')
def init_page():
    return 'init page'

@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)

if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()
