#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask import Flask, render_template, request
from livereload import Server

app = Flask(__name__)

@app.route('/')
def extends_test():
    return render_template('child_1.html', title='child-1')

@app.route('/about')
def about():
    return 'about'

# 创建jinja2测试函数
@app.template_test('current_link')
def is_current_link(link):
    return link['href'] == request.path

if __name__ == '__main__':
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=False)