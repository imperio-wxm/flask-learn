#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'wxmimperio'

from flask import Flask,render_template,make_response,request

app = Flask(__name__)

@app.route('/login',methods=['POST','GET'])
def login():
    response = make_response(render_template('login.html'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 写入cookie
        response.set_cookie(username,password)
        return response
    return render_template('login.html')

@app.errorhandler(404)
def page_not_found(error):
    # 可以直接指定错误码
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
