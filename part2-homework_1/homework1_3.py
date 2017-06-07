# coding# -*- coding:utf-8 -*-

# Readme
# Author: Elijah
# Time: 2017-05-31
# Function: 输出 1-100 内的所有奇数
# Need Environment：Python 3.5 、PyCharm
# Move：
# Feature：
# Important py file：
# How To：Execute directly
# 个人发挥：
# 个人博客地址：http://write.blog.csdn.net/mdeditor#!postId=72835866

# Method 1:
for i in range(101):  #用for循环，从0循环100
    if i % 2 == 1:  #如果i对2取余等于1，说明i为奇数
        print(i)

# # Method 2:
count = 0
while count < 100 : #用while在100内循环
    count += 1  #设置count计数器
    if count % 2 == 1 : #如果计数器count对2取余等于1，说明count为奇数
        print(count)

