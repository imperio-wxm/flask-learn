#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "wxmimperio"

from flask_login import UserMixin

from . import db, login_manager
from datetime import datetime


class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    users = db.relationship('User', backref='role')

    @staticmethod
    def seed():
        db.session.add_all(map(lambda r : Roles(name=r), ['Guests','Administrators']))
        db.session.commit()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(20), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @staticmethod
    def on_created(target, value, oldvalue, initiator):
        target.role = Roles.query.filter_by(name='Guests').first()

# 挂钩函数
@login_manager.user_loader()
def load_user(user_id):
    return User.query.get(int(user_id))


db.event.listen(User.name,'set',User.on_created)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    body = db.Column(db.String(100))
    body_html = db.Column(db.String(100))
    created = db.Column(db.DateTime, index=True,default=datetime.utcnow)

    @staticmethod
    def on_body_changed(target, value, oldvalue, initiator):
        target.body_html = value

db.event.listen(Post.body,'set',Post.on_body_changed)


class Comnet(db.Model):
    __tablename__ = 'coments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(100))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow())