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

import socket
import time

s = socket.socket()
s.bind(('127.0.0.1', 8000))  # 绑定ip和端口
s.listen()  # 最大监听数量


def shandi(url):  # 通过路径返回不同的值的函数
    return "欢迎来到山地车界面/{}".format(url)


def gonglu(url):  # 通过路径返回不同的值的函数
    return "欢迎来到公路车界面/{}".format(url)


def yueyegonglu(url):  # 通过路径返回不同的值的函数
    return "欢迎来到越野公路界面/{}".format(url)


def home(url):
    # # 通过socket返回整个html给浏览器客户端的函数
    with open('home.html', 'r', encoding='utf-8') as f:
        rets = f.read()
        return rets


def timer(url):
    with open('time.html', 'r', encoding='utf-8') as f:
        rets = f.read()
        times = time.localtime()
        times = time.strftime("%y-%m-%d %H:%M:%S", times)
        return rets.replace('@@time@@', times)


lists = [
    ('/shandi', shandi),
    ('/gonglu', gonglu),
    ('/yueyegonglu', yueyegonglu),
    ('/home', home),
    ('/time', timer)
]

# while True:
#     sk, addr = s.accept()  # 接收请求
#     # print(addr)
#     data = sk.recv(2048).decode('utf-8')
#     #  根据路径返回不同结果
#     url = data.split()[1]
#     # print(data)
#     # sk.send(b'http/1.1 200 OK\r\ncontent-type: text/html; charset=utf-8\r\n\r\n')
#     # content-type: text/html; charset=utf-8 这个响应头部告诉浏览器返回的是text/html 文件格式，编码格式是utf-8，方式出现乱码
#     # if url == '/shandi':
#     #     sk.send(b'/shandi/')
#     # elif url == '/gonglu':
#     #     sk.send(b'/gonglu/')
#     # else:
#     #     sk.send(b'404 not fund')
#     func = None
#     for i in lists:
#         if i[0] == url:
#             func = i[1]
#             break
#     if func:
#         ret = func(url)
#         sk.send(b'http/1.1 200 OK\r\ncontent-type: text/html; charset=utf-8\r\n\r\n')
#     else:
#         ret = '404 not found'
#         sk.send(b'http/1.1 404 FAIL\r\ncontent-type: text/html; charset=utf-8\r\n\r\n')
#     sk.send(ret.encode('utf-8'))
#
#     sk.close()


if __name__ == '__main__':
    options = {
        ('1', '2'): '3',
        ('4', '5'): '6'
    }
    print(options[('1', '2')])
