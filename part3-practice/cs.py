# /usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "Elijah"
__date__ = "2017/6/13 20:19"


# 第二模块、升阶考核
#
# 8 bit = 1 byte
# AbcDef
# abc_def
# global
#
# n = u "老男孩" ——>unicode
# m = n.encode("utf-8")
# m.decode("utf-8").encode("gbk")
#
# for i in range(1,101):
#     if i % 2 == 1:
#         print(i)
#
# n=(11,22,33,44,["bb","cc","dd",{"a1":[1,2,3],"b1":"3"}])
#
# # n[4][3]["a1"] = [1,2,3,4]
# # print(n)
#
# #
# # lst = [1,2,3,4]
# # print(lst.__dir__())
#
# n[4][3]["a1"].append(4)
# print(n)

# a = 1
# b = 2
#
# res = a if a < b else b
# print(res)
#
# if a < b :
#     print(a)
# else:
#     print(b)

# lst=["11","22","33"]
#
# str = '_'.join(lst)
# print(str)

# int
# str
# tuple

###########################列表生成式

############### s="天气%%真好%s" #%转义
# a=s%("么")
# print(a)

########### .pyc #py当做模块被其他py引用时候

# str="aabbaaccddeeaabb"
#
# print(str.replace('aa','ff'))


# import time
# def deco(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         func()
#         stop = time.time()
#         print("run time is %s" %(stop -start))
#     return wrapper
# @deco #index = deco(index)
# def index():
#     print("welcome to oldboy!")
# index()


# #-------------------装饰器有问题的--------------------------
# def outer(func):
#     print('1')
#     func()
#     print('2')
#     return func
#
# @outer
# def f1():
#     print("原函数f1")

# @outer
# def f2():
#     print("原函数f2")
#
# f2()
# '''
# 或者我们还可以看一下这个例子，两个原函数，我只调用f2同时f2有outer这个所谓的"一层装饰器"
# 结果如下，outer(f1)、outer(f2)、f2都被调用了，这也证明了刚才的说法
# '''
# -------------------------------------------

# #-----------------------装饰器没问题的--------------------
# def outer(func):
#     def inner():
#         print('1')
#         func()
#         print('2')
#     return inner
#
# @outer
# def f1():
#     print("原函数f1")
#
# @outer
# def f2():
#     print("原函数f2")
# f2()
# '''
# 正常的装饰器，调用f2同时f2有outer这个装饰器的时候，
# 其他的无关的函数并没有一并执行，只是单纯的为f2加了装饰器
# '''
# #-------------------------------------------


