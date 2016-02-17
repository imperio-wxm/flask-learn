#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask_wtf import Form
from wtforms import PasswordField,StringField,SubmitField
from wtforms.validators import DataRequired

class loginForm(Form):
    # 设置字段不为空
    username = StringField(label=u'用户名：',validators=[DataRequired()])
    password = PasswordField(label=u'密码：',validators=[DataRequired()])
    submit = SubmitField(label=u'提交')