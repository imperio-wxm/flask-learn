#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask import Flask,render_template
from livereload import Server
from flask_wtf_form import loginForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
# 读取外部配置文件
app.config.from_pyfile('config')

@app.route('/',methods=['POST','GET'])
def loginTest():
    # 引入登陆方法
    form = loginForm()
    return render_template('flask_wtf_form.html',form=form,title=u'登陆')

if __name__ == '__main__':
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=False,debug=True)