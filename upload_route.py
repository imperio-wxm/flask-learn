#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'wxmimperio'

from flask import Flask, request,redirect,url_for,render_template
from os import path
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        # 获取当前路径的绝对路径
        base_path = path.abspath(path.dirname(__file__))
        # 目标文件存放的位置
        upload_path = path.join(base_path,'static/uploads',secure_filename(f.filename))
        f.save(upload_path)
        return redirect(url_for('upload'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
