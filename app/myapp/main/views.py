#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask import render_template,request
from . import main

@main.route('/')
def index():
    return render_template('index.html',title=u'欢迎')

@main.route('/about')
def about():
    return render_template('about.html',title=u'关于')

@main.route('/admin')
@login_required
def admin():
    return 'Admin'