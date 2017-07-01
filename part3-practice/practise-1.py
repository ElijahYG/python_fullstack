#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Elijah"
__date__ = "2017/6/9 21:28"

import time

def timmer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        res = func()
        stop = time.time()
        print("tun time is %s" %(stop -start))
    return wrapper


@timmer  # timmer就是装饰器，只要写了@decorate，就会将@decorate下面的一行的函数名当做参数传给装饰器，index = timmer(index)
def index():
    time.sleep(3)
    print("welcome to oldboy!")
index() #本质就是执行的wrapper()