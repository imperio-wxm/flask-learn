#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask import render_template,request
from flask.ext.login import  login_required, current_user
from .forms import CommentForm, PostForm
from flask_babel import gettext as _
from  .. import db
from ..models import Post, Comment
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

@main.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

@main.app_template_test('current_link')
def is_current_link(link):
    return link == request.path

@main.route('/posts/<int:id>', method=['GET','POST'])
def post(id):
    # detail 详情
    post = Post.query.get_or_404(id)

    # 评论
    form = CommentForm()

    # 保存评论
    if form.validate_on_submit():
        comment = Comment(author=current_user,body=form.body.data,post=post)
        db.session.add(comment)
        db.session.commit()

    return  render_template('posts/detail.html',title=post.title,form=form,post=post)