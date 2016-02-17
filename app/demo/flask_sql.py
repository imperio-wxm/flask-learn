#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template
from os import path
from flask.ext.script import Manager,Shell

app = Flask(__name__)
manager = Manager(app)

# 当前项目绝对路径
basedir = path.abspath(path.dirname(__file__))

# 数据库连接
app.config.from_pyfile('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/flask_db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route('/')
def sqlAlchemy_test():
    return render_template('sql_test.html')

# 数据库映射
class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    # 主键关联
    users = db.relationship('Users',backref='role')

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    passwd = db.Column(db.String(20), nullable=True)
    # 外键关联
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()