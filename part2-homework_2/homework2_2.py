# -*- coding:utf-8 -*-

# Readme
# Author: Elijah
# Time: 2017-05-31
# Function: 三级菜单：
#     1. 运行程序输出第一级菜单
#     2. 选择一级菜单某项，输出二级菜单，同理输出三级菜单
#     3. 返回上一级菜单和顶部菜单
#     4. 菜单数据保存在文件中
#
# Need Environment：Python 3.5 、PyCharm
# Move：
# Feature：
#    1、
#    2、
#    3、
# Important py file：getpass
# How To：Execute directly
# 个人发挥：
# 个人博客地址：http://blog.csdn.net/dragonyangang/article/details/72851011

import json

with open("menu_serialize.json",mode="r",encoding="utf-8") as f :
    menu = json.loads(f.read())

current_layer = menu #保存字典

last_layer = [ menu ] #设置列表存储上一层

while True:
    for key in current_layer: #输出字典第一层
        print(key)
    choice = input("Input your choice (input 'b' to Back last layer, 'q' to Quit)==>").strip()  #用户输入
    if len(choice) == 0 : #如果用户没有输入，则跳出本次循环
        continue
    if choice in current_layer:
        last_layer.append(current_layer) #进入下层字典之前，先将本层保存至列表
        current_layer = current_layer[choice] #将下层赋值给current_layer
    if choice.lower() == 'b': #用户返回上一层操作
        if last_layer:
            current_layer = last_layer[len(last_layer)-1] #选择完成后将列表中最后一个值赋给current_layer当前层
            last_layer.pop()
    if choice.lower() == 'q':
        exit()

