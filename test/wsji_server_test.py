# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       eddie
   date：          2021/3/2
-------------------------------------------------
   Change Activity:
                   2021/3/2:
-------------------------------------------------
"""
__author__ = 'eddie'

import time
from wsgiref.simple_server import make_server
from jinja2 import Template


def index(url):
    filename = ['山地', '公路', '越野']
    with open('home.html', 'r', encoding='utf-8') as f:
        s = f.read()
        template = Template(s)  # 加载模板
        ret = template.render(filename=filename)  # 渲染模板
        return bytes(ret, encoding='utf-8')


def timrs(url):
    with open('time.html', 'r', encoding='utf-8') as f:
        s = f.read()
        s = s.replace('@@time@@', time.strftime("%Y-%m-%d %H:%M:%S"))
    return bytes(s, encoding='utf-8')


lists = [("/index", index),
         ("/timer", timrs)]


def run_server(environ, start_response):
    start_response("200 ok", [('Content-Type', 'text/html; charset=utf-8'), ])
    url = environ['PATH_INFO']
    print(url)
    func = None
    for i in lists:
        if i[0] == url:
            func = i[1]
            break
    if func:
        response = func(url)
    else:
        response = b"404 not fund"
    return [response, ]


if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8090, run_server)
    print('8090。。。。。')
    httpd.serve_forever()
