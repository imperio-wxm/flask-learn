#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'wxmimperio'

from flask import Flask
from werkzeug.routing import BaseConverter

# 正则表达式过滤定义
class RegexConverter(BaseConverter):
    def __init__(self,url_map,*items):
        super(RegexConverter,self).__init__(url_map)
        self.regex=items[0]

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter

# 正则表达式过滤规则
@app.route('/user/<regex("([a-z]{3})"):user_name>')
def user_name(user_name):
    return 'username = %s' % user_name

if __name__ == '__main__':
    app.run(debug=True)