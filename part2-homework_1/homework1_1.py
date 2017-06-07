# -*- coding:utf-8 -*-

# Readme
# Author: Elijah
# Time: 2017-05-31
# Function: 使用while循环输出 1 2 3 4 5 6     8 9 10
# Need Environment：Python 3.5 、PyCharm
# Move：
# Feature：
# Important py file：
# How To：Execute directly
# 个人发挥：
# 个人博客地址：http://write.blog.csdn.net/mdeditor#!postId=72835866

# Method 1:
count = 0
while True :  #用while设置死循环
    count += 1
    if count == 7 :   #如果count等于7，跳出本次循环
        continue
    print(count)
    if count == 10 :  #如果count等于10，则将其重置为0，继续循环
        count = 0
# Method 2:
count = 0
while True : #用while设置死循环
    while count < 10 : #用第二层循环是之在10内循环
        count += 1
        if count != 7 :  #如果count不等于7则输出，否则不输出
            print(count)
    count = 0  #重置count进行下一次的10内循环




