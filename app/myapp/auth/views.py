#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask import render_template, redirect,url_for

from . import auth
from . import forms
from .forms import RegistrationForm
from .. import db
from ..models import User


# 引用蓝图
@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html',title=u'登录',form=forms)

@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    # 表单提交创建用户
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    name=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.submit()
        # url_for中须添加蓝图名字
        return redirect(url_for('auth.login'))
    return render_template('register.html',title=u'注册',form=form)