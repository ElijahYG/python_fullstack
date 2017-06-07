# coding=utf-8# coding# -*- coding:utf-8 -*-

# Readme
# Author: Elijah
# Time: 2017-05-31
# Function: 求1-2+3-4+5 ... 99的所有数的和
# Need Environment：Python 3.5 、PyCharm
# Move：
# Feature：
# Important py file：
# How To：Execute directly
# 个人发挥：
# 个人博客地址：http://write.blog.csdn.net/mdeditor#!postId=72835866

# Method 1:
result = 0
for i in range(100):  #用for循环，从0循环99
    if i % 2 == 0:  #如果i对2取余等于0，说明i为偶数，并将其减去
        result = result - i
    else:
        result = result + i #否则如果i对2取余不等于0，说明i为奇数，并将其加上
print(result)

# Method 2:
result = 0
count = 0
while count < 99 : #用while在99内循环
    count += 1  #设置count计数器
    if count % 2 == 0 : #如果计数器count对2取余等于0，说明count为偶数，并将其减去
        result = result - count
    else:
        result = result + count #如果计数器count对2取余不等于0，说明count为奇数，并将其加上
print(result)

