#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask import render_template
from . import auth

# 引用蓝图
@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html',title=u'登录',form=form)

@auth.route('/register',methods=['GET','POST'])
def register():
    return render_template('register.html',title=u'注册')