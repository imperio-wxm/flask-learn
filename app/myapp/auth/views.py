#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask import render_template

from . import auth
from . import forms


# 引用蓝图
@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html',title=u'登录',form=forms)

@auth.route('/register',methods=['GET','POST'])
def register():
    form = forms.RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    name=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.submit()

        return redirect(ur)
    return render_template('register.html',title=u'注册')