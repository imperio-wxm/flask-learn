#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', title='Hello')

@app.route('/about')
def about():
    return 'about'

if __name__ == '__main__':
    app.run(debug=True)