#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'wxmimperio'

from flask import Flask,render_template
from livereload import Server
from markdown import markdown

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='<h1>Hello World</h1>',
                           body='- python Header2')

# 过滤器装饰，过滤器名字叫md
@app.template_filter('md')
def markdown_to_html(txt):
    return markdown(txt)

def read_file(filename):
    with open(filename) as file:
        content = reduce(lambda x,y:x+y,file.readlines())
    return content.decode('utf-8')

# 上下文处理器
# 在模板渲染前使用
@app.context_processor
def inject_methods():
    return dict(read_file=read_file)

if __name__ == '__main__':
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)
