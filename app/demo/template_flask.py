#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', title='Hello')

@app.route('/about')
def about():
    return 'about'

# 简单动态路由
@app.route('/user/<username>')
def user(username):
    return username
@app.route('/user/<int:user_id>')
def user_id(user_id):
    return 'user_id %d' % user_id

# 制定多个路由规则
# 默认是指向index或者default
@app.route('/user/info/')
@app.route('/user/information/')
def user_info():
    return 'user info is right'

if __name__ == '__main__':
    app.run(debug=True)
