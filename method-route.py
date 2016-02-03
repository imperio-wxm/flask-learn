#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'wxmimperio'

from flask import Flask, render_template,request

app = Flask(__name__)

# GET
"""
浏览器告知服务器：只获取页面上的信息并发送给我（最常用的方法）
"""
# POST
"""
浏览器告诉服务器：想在URL上发布新信息，并且服务器必须确保数据已经存储，且仅存储一次
这是HTML表单通常发送数据到服务器的方法
"""
# PUT
"""
类似POST，但是服务器可能触发了存储过程多次，多次的操作会覆盖掉旧值
"""

@app.route('/login',methods=['GET','POST'])
def login():
    # 获取表单数据
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    else:
        username = request.args['username']
        password = request.args['password']
    print username,password
    return render_template('login.html',method=request.method)
if __name__ == '__main__':
    app.run(debug=True)
