#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask_wtf import Form
from wtforms import PasswordField,StringField
from wtforms.validators import DataRequired

class loginForm(Form):
    # 设置字段不为空
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])