# -*- coding:utf-8 -*-

# Readme
# Author: Elijah
# Time: 2017-05-31
# Function: 模拟登陆
#     1. 用户输入帐号密码进行登陆
#     2. 用户信息保存在文件内
#     3. 用户密码输入错误三次后锁定用户
#
# Need Environment：Python 3.5 、PyCharm
# Move：
# Feature：
#    1、开始提供用户选择功能界面：登陆 or 注册
#    2、用户在输入用户名或者密码时可以中断退出
#    3、用户名和密码是对应的，所以判断用户和密码是否正确时要对应判断
#    4、用户注册时要判断用户名是否已经被注册，已经被注册的不能再次注册
#    5、单独有一个文件存储被锁定的用户名，以提供用户检查
# Important py file：getpass
# How To：Execute directly
# 个人发挥：
# 个人博客地址：http://blog.csdn.net/dragonyangang/article/details/72835866


import getpass

r_flag = False
l_flag = False
count = 0
while True:
# 用户选择界面，可以进行注册、登陆和退出
    choice = input("Input 'R' to Register \nInput 'L' to Login \nInput 'Q' to Quit \n:")
#用户登陆功能
    if choice.lower() == "l" :
        while True:
            username = input("Input your username (or 'Q' for exit):").strip()
            if username.lower() == "q":
                exit()
            password = getpass.getpass("Input your password (or 'Q' for exit):").strip()
            if password.lower() == "q":
                exit()
            with open("user_locked.txt", mode="r", encoding="utf-8") as f_locked: #判断用户是否在锁定名单中
                for line in f_locked:
                    if line.startswith("username:") and username in line:
                        print("This username has been locked , please contact Administrator !")
                        exit() #用户名被锁定，程序退出
            with open("user_info.txt", mode="r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("username:") and username in line:
                        l_flag = True  #对应的用户名一定在密码的上一行，若用户名正确，flag赋值为true，继续判断对应的密码
                        continue #跳出本次循环，读取下一行密码
                    if l_flag:
                        if line.split(":")[1].strip() == password : #若用户名对应的密码也正确，则登陆成功
                            print("Welcome " + username + " ! " + " Login Successful !")
                            exit()
                        elif count >= 3: #判断如果输入错误次数大于3次，则将用户加入至锁定名单
                            with open("user_locked.txt", mode="a", encoding="utf-8") as f_locked:
                                f_locked.write("\nusername:" + username)
                                print(
                                    "Sorry, you've try more than 3 times , "
                                    "this username will be added in locked_list , "
                                    "please contact Administrator !")
                                exit()
                        else:
                            l_flag = False
                            count += 1   #计数器，若count加至3，则用户尝试登陆次数过多，强制返回选择界面！
                            print("incorrect username or password !")
                            break #退出文本循环，用户重新输入用户名和密码
#用户注册功能
    if choice.lower() == "r" :
        while True:
            new_username = input("Input new username (or 'Q' for exit):").strip()
            if new_username.lower() == "q":
                exit()
            new_password = getpass.getpass("Input new password (or 'Q' for exit):").strip()
            if new_password.lower() == "q":
                exit()
            with open("user_info.txt", mode="r+", encoding="utf-8") as f:
                f.seek(0) #光标重置至开头
                for line in f:
                    if line.startswith("username:") and new_username in line: #判断用户名是否已经存在，存在则不能注册
                        print("Sorry ! This username is already exist , please change !")
                        r_flag = True
                        break #用户名已经存在，不能注册，跳出循环重新输入
                if r_flag : #如果用户输入的用户名已经存在，则退出重新输入用户名，此处为注册标志位，退出本次循环
                    r_flag = False #注册标志重置
                    continue
                f.write("username:" + new_username + "\n")
                f.write("password:" + new_password + "\n")
                print("Congratulation ! " + new_username + " Register Successful !")
                break #用户注册成功，返回用户选择界面，用户可以选择登陆、继续注册或退出
#用户退出功能
    if choice.lower() == "q":
        exit() #用户退出
