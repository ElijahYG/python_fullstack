#!/usr/bin/env python
# !_*_ coding:utf-8 _*_
__author__ = "Elijah"
__date__ = "2017/6/9 21:28"

# import time
#
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         res = func()
#         stop = time.time()
#         print("tun time is %s" %(stop -start))
#     return wrapper
#
#
# @timmer  # timmer就是装饰器，只要写了@decorate，就会将@decorate下面的一行的函数名当做参数传给装饰器，index = timmer(index)
# def index():
#     time.sleep(3)
#     print("welcome to oldboy!")
# index() #本质就是执行的wrapper()

# 按位置
# 按关键字
# 混合

# def test(*args):
#     print(*args)
# l = [1,2,3]
# test(l)

# def test():
#     res = 0
#     for i in range(1,101,2):
#         res += i*(i+1)
#     print(res)
# test()


# def deco(func):
#     def wrapper(*args):
#         print("before")
#         func(*args)
#         print("after")
#     return wrapper
#
# @deco
# def f1(arg):
#     return arg + 1
#
# @deco
# def f2(arg1, arg2):
#     return arg1 + arg2
#
# f1(1)
# f2(1,2)

# import  random
# def randomnum():
#     s = ""
#     i = 0
#     while i < 6:
#         s += str(random.randint(0,9))
#         i +=1
#     print(s)
#
# randomnum()


# import string
# print(string.digits)


# def deco(func):
#     def wrapper(*args,**kwargs):
#         print('------>before')
#         func(*args)
#         print('------>after')
#     return wrapper
#
# @deco
# def f1(arg):
#     print(arg + 1)
#
# @deco
# def f2(arg1, arg2):
#     print(arg1 + arg2)
#
# f1(1)
# f2(1,2)

# def cover(name):
#     def decorate(func):
#         def wrapper(*args,**kwargs):
#             if name == 'user1':
#                 print("----->first %s"%name)
#                 func()
#                 print("----->after %s"%name)
#             elif name=='user2':
#                 print("----->first %s"%name)
#                 func()
#                 print("----->after %s"%name)
#             else:
#                 print("Who are you?")
#         return wrapper
#     return decorate
#
# @cover(name ='user1')
# def f1():
#     print("user1 original function !!!")
#
# @cover(name ='user2')
# def f2():
#     print("user2 original function !!!")
#
#
# f1()
# print('\n')
# print('=='*20)
# print('\n')
# f2()

# d={"a":1, "b":2, "c":3}
# print(d.__iter__().__next__())
# print(next(iter(d)))
# print(next(iter(d.values())))
# print(iter(d))

# def f(x):
#     return x**2
#
# r= map(f,[1,2,3])
# print(r)

'''
浅拷贝：增加一个内存指针指向前一个内存
深拷贝：增加一个内存指针并申请一块新的内存
'''
# import sys
# print(sys.path)

'''
1、存储元素的数据结构就可以称作可迭代对象
2、具有__next__方法的都可以称作迭代器
3、拥有yield都称作生成器，也是迭代器
'''

# l = [i for i in range(1,100)]
# print(l)
# g = (i for i in range(1,100))

# def deco(func):
#     def wrapper(args):
#         print('你好')
#         func(args)
#         print('再见')
#     return wrapper
#
# @deco
# def test1(arg):
#      return arg +1
#
# test1(1)

# import random,string
#
# def test():
#     # s= string.printable
#     # l = list(s)
#     s = string.ascii_letters + string.digits + string.punctuation
#     index = random.sample(s, 6)
#     st = "".join(index)
#     print(st)
#
# test()

# import random
# def test():
#     i = 0
#     for i in range(0,6):

list1 = [11,22,33,44,55]
list2 = [1,2,3,4,5]
#
# def add(arg):
#     return arg+100
# lst = map(add,list1)
# print(list(lst))

print(list(zip(list1,list2)))





