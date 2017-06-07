# -*- coding:utf-8 -*-

# Readme
# Author: Elijah
# Time: 2017-05-31
# Function: 求1-100的所有数的和
# Need Environment：Python 3.5 、PyCharm
# Move：
# Feature：
# Important py file：
# How To：Execute directly
# 个人发挥：
# 个人博客地址：http://blog.csdn.net/dragonyangang

# Method 1:
count = 0
result = 0
while count < 100: #用while在100内循环
    count += 1     #计数器每次加1
    result = result + count #用result将每次计数器的结果相加
print(result)

# Method 2:
result = 0
for i in range(101):  #用for循环，从0循环100
    result = result + i  #用result将每次循环的值相加保存
print(result)