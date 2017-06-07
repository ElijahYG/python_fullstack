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
op_flag = False
count = 0


while not op_flag:
    # 用户选择界面，可以进行注册、登陆和退出
    choice = input("Input 'R(Register)' to Register \nInput 'L(login)' to Login \nInput 'Q(quit)' to Quit \n>>>")
    # 用户登陆功能
    if choice.lower() == "l":
        while True:
            username = input("Input your username (or 'Q' for exit):").strip()
            if username.lower() == "q":
                op_flag = True
                print("end".center(40, "-"))
                break
            password = getpass.getpass("Input your password (or 'Q' for exit):").strip()
            if password.lower() == "q":
                op_flag = True
                print("end".center(40, "-"))
                break
            # 判断用户是否在锁定名单中
            with open("user_locked.txt", mode="r", encoding="utf-8") as f_locked:
                for line in f_locked:
                    if line.startswith("username:") and username in line:
                        print("This username has been locked , please contact Administrator !")
                        break
            with open("user_info.txt", mode="r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("username:") and username in line:
                        l_flag = True
                        continue
                    if l_flag:
                        # 若用户名对应的密码也正确，则登陆成功
                        if line.split(":")[1].strip() == password:
                            print("Welcome " + username + " ! " + " Login Successful !")
                            exit()

                        # 判断如果输入错误次数大于3次，则将用户加入至锁定名单
                        elif count >= 3:
                            with open("user_locked.txt", mode="a", encoding="utf-8") as f_locked:
                                f_locked.write("username:" + username + "\n")
                                print(
                                    "Sorry, you've try more than 3 times , "
                                    "this username will be added in locked_list , "
                                    "please contact Administrator !")
                                exit()
                        else:
                            l_flag = False
                            # 计数器，若count加至3，则用户尝试登陆次数过多，强制返回选择界面！
                            count += 1
                            print("incorrect username or password !")
                            break
                    else:
                        print(" Incorrect username or password ! "
                              "Please ensure you have Account ! You can retry and input 'R' to register .")
                        exit()
    # 用户注册功能
    elif choice.lower() == "r":
        while True:
            new_username = input("Input new username (or 'Q' for exit):").strip()
            if new_username.lower() == "q":
                exit()
            new_password = input("Input new password (or 'Q' for exit):").strip()
            if new_password.lower() == "q":
                exit()
            with open("user_info.txt", mode="a+", encoding="utf-8") as f:
                f.seek(0)
                for line in f:
                    if line.startswith("username:") and new_username in line:
                        print("Sorry ! This username is already exist , please change !")
                        r_flag = True
                        break
                if r_flag:
                    r_flag = False
                    continue
                f.write("username:" + new_username + "\n")
                f.write("password:" + new_password + "\n")
                print("Congratulation ! " + new_username + " Register Successful !")
                break
    # 用户退出功能
    elif choice.lower() == "q":
        op_flag = True
    else:
        print("确认输入的是否正确")


# 代码中尽量不要有太多exit()
# 代码中开头代码中的注释，写到readme中，每一个小的项目都要有一个readme让我知道它是干什么的，而不是代码中说明
# 字符串拼接不要用+好  ，用字符串传参
# 看看我给你修改了什么，不必要的说明不要写，单间的一个break  continue  count等信息不要写备注，乱
# 虽然pep8中规定，代码的最后可以用#号加注释，但是还是建议在代码上方或下发对应缩进注释，要不会显示代码很乱