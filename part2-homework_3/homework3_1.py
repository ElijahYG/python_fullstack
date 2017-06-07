# -*- coding:utf-8 -*-

# Readme
# Author: Elijah
# Time: 2017-06-3
# Function:购物车
#     1. 商品信息- 数量、单价、名称
#     2. 用户信息- 帐号、密码、余额
#     3. 用户可充值
#     4. 购物历史信息
#     5. 允许用户多次购买，每次可购买多件
#     6. 余额不足时进行提醒
#     7. 用户退出时 ，输出当次购物信息
#     8. 用户下次登陆时可查看购物历史
#     9. 商品列表分级显示
#
# Need Environment：Python 3.5 、PyCharm
# Move：
# Feature：
# Important py file：json, getpass,time
# How To：Execute directly
# 个人发挥：
# 个人博客地址：http://blog.csdn.net/dragonyangang/article/details/72862830

import time, getpass

# 商品清单(字典)
product_list = {
    '服装': {
        '外套': {
            '皮衣': {
                '加绒皮衣': {'price': 2000, 'num': 0, 'sum': 10},
                '机车皮衣': {'price': 1000, 'num': 0, 'sum': 10},
                '牛皮皮衣': {'price': 1500, 'num': 0, 'sum': 10},
                '羊皮皮衣': {'price': 1800, 'num': 0, 'sum': 10},
            },
            '风衣': {
                '立领风衣': {'price': 500, 'num': 0, 'sum': 10},
                '双层领风衣': {'price': 800, 'num': 0, 'sum': 10},
            }
        },
        '西装': {
            '休闲西装': {
                '韩版休闲西装': {'price': 600, 'num': 0, 'sum': 10},
                '欧美风休闲西装': {'price': 500, 'num': 0, 'sum': 10},
            },
            '宴会西装': {
                '修身燕尾服': {'price': 1200, 'num': 0, 'sum': 10},
                '宫廷装': {'price': 1000, 'num': 0, 'sum': 10},
            },
        },
        '裤子': {
            '休闲裤': {
                '修身休闲裤': {'price': 300, 'num': 0, 'sum': 10},
                '宽松休闲裤': {'price': 280, 'num': 0, 'sum': 10},
            },
            '牛仔裤': {
                '紧身牛仔裤': {'price': 180, 'num': 0, 'sum': 10},
                '镂空牛仔裤': {'price': 230, 'num': 0, 'sum': 10},
            },
        },
    },
    '家电': {
        '电视': {
            "液晶电视": {
                '32寸液晶电视': {'price': 1400, 'num': 0, 'sum': 10},
                '42寸液晶电视': {'price': 2200, 'num': 0, 'sum': 10},
                '55寸液晶电视': {'price': 4500, 'num': 0, 'sum': 10},
            },
            "网络电视": {
                '2K网络电视': {'price': 1500, 'num': 0, 'sum': 10},
                '4K网络电视': {'price': 3200, 'num': 0, 'sum': 10},
                '曲面网络电视': {'price': 4600, 'num': 0, 'sum': 10},
            }
        },
        '空调': {
            '挂壁式空调': {
                '冷暖型挂壁式空调': {'price': 1600, 'num': 0, 'sum': 10},
                '单冷型挂壁式空调': {'price': 1800, 'num': 0, 'sum': 10},
            },
            '柜式空调': {
                '2匹柜式式空调': {'price': 4000, 'num': 0, 'sum': 10},
                '3匹柜式式空调': {'price': 6000, 'num': 0, 'sum': 10},
            },
        },
    },
}

# 用于储存已选中商品
shopping_cart = []

# 用于分级显示
current_layer = product_list
last_layer = [product_list]

# 用户存储用户购物信息，用户购物结束输出
bill = []

# 标志位、计数器
r_flag = False
l_flag = False
count = 0
count_layer = 0
total_cost = 0

while True:
    # 用户选择界面，可以进行注册、登陆和退出
    choice = input("Input 'R' to Register \nInput 'L' to Login \nInput 'Q' to Quit \n:")
    # 用户登陆功能
    if choice.lower() == "l":
        while True:
            username = input("Input your username (or 'Q' for exit):").strip()
            if username.lower() == "q":
                exit()
            password = getpass.getpass("Input your password (or 'Q' for exit):").strip()
            if password.lower() == "q":
                exit()
            with open("user_locked.txt", mode="r", encoding="utf-8") as f_locked:  # 判断用户是否在锁定名单中
                for line in f_locked:
                    if line.startswith("username:") and username in line:
                        print("This username has been locked , please contact Administrator !")
                        exit()  # 用户名被锁定，程序退出
            with open("user_info.txt", mode="r+", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("username:") and username in line:
                        l_flag = True  # 对应的用户名一定在密码的上一行，若用户名正确，flag赋值为true，继续判断对应的密码
                        continue  # 跳出本次循环，读取下一行密码
                    if l_flag:
                        if line.split(":")[1].strip() == password:  # 若用户名对应的密码也正确，则登陆成功
                            # ------------------------->登陆成功开始进入购物功能
                            print("Welcome " + username + " ! " + " Login Successful !")
                            cash = int(f.readline().split(":")[1].strip())  # 从文件中取出用户的cash余额
                            f.seek(0)
                            Consup_hist = f.read() #读取用户的历史购买记录至字符串中
                            Consup_hist = Consup_hist[Consup_hist.index('\n',Consup_hist.index(username+'_cash')):
                            Consup_hist.index('username',Consup_hist.index(username+'_cash'))]
                            print("\nConsumption history below：" + "\n" + Consup_hist)
                            Consup_hist = ''
                            print("\nYour Balance is :" + str(cash))
                            if cash == 0:  # 如果用户余额为0，则让其输入初始金额
                                cash = int(input("Please input your available cash:").strip())
                            while True:
                                if 0 <= count_layer <= 3:  # 商品字典有4级，用计数器控制进入字典的层级数
                                    print("\n目前是第" + str(count_layer + 1) + "层商品目录")
                                    for key in current_layer:
                                        print(key)
                                    choice = input("Input the Product Name you want to buy or "
                                                   "input 'B' to back or "
                                                   "input 'Q' to quit：").strip()
                                    if choice in current_layer:
                                        last_layer.append(current_layer)  # 更新当前层之前，保存
                                        current_layer = current_layer[choice]
                                        count_layer += 1
                                    if choice.lower() == 'b':  # 用户返回上一层商品字典
                                        if last_layer:
                                            if count_layer > 0:  # 将字典层数减1
                                                count_layer -= 1
                                            current_layer = last_layer[len(last_layer) - 1]  # 也可以直接last_layer[-1]
                                            last_layer.pop()
                                            continue  # 跳出本次循环，用户进入上一层继续选择商品字典
                                    if choice.lower() == 'q':  # 用户选择退出
                                        f.close()  # 首先关闭打开的文件，准备后面更新文件信息
                                        print("Your Bill :\n名称\t数量")  # 输出用户本次购物信息
                                        for i in bill:
                                            print(i)
                                        print("Total Cost : " + str(total_cost))
                                        print("Balance : " + str(cash))
                                        print("\nLooking forward to your next visit !!!")
                                        with open("user_info.txt", mode="r", encoding="utf-8") as f:  # 更新文件中的cash
                                            old_info = f.read()
                                            new_info = old_info.replace(
                                                (old_info[old_info.index(username + '_cash', old_info.index(username))
                                                :old_info.index('\n', old_info.index(username + '_cash'))]),
                                                (username + '_cash:' + str(cash) + '\n'))
                                        with open("user_info.txt", mode="w", encoding="utf-8") as f:  # 写入新的cash余额
                                            f.write(new_info)
                                        exit()
                                else:  # 进入最后一层商品目录，显示单价和数量，提问用户选择是否购买
                                    print('单价：' + str(current_layer['price']),
                                          '\n已购数量：' + str(current_layer['num']),
                                          '\n库存数量：' + str(current_layer['sum']), )
                                    is_buy = input("\nIf you decided to buy ,please input 'Y' "
                                                   "or input 'B'to back "
                                                   "or 'Q' to quit")
                                    if is_buy.lower() == 'y':  # 用户确认购买
                                        buy_num = input("Please input the Number you want to buy :").strip()  # 输入数量
                                        if buy_num.isdigit():
                                            if cash >= current_layer['price'] * int(buy_num):  # 用户余额足够时
                                                count_layer = 0  # 将字典层级数重置
                                                cash -= current_layer['price'] * int(buy_num)  # 扣除金额
                                                current_layer['num'] += int(buy_num)  # 更新字典中对应的购买数量
                                                current_layer['sum'] -= int(buy_num)  # 更新字典中对应的库存数量
                                                print("\nAdded " + str(buy_num) + " * " + choice +
                                                      " into shopping cart ! Now your current cash is " +
                                                      str(cash))
                                                # 将本次购物信息写入列表，用于结束购物输出本次购物信息
                                                bill.append([choice, current_layer['num']])
                                                total_cost += current_layer['price'] * int(buy_num)
                                                # 将本次购物信息写入文件，用于历史输出,将文件重新读入，字符串中间拼接后回存
                                                f.close()
                                                with open("user_info.txt", mode="r",encoding="utf-8") as f:
                                                    old_history = f.read()
                                                    new_history = old_history[0:old_history.index('\n',old_history.index(username+'_cash'))] +\
                                                                  "\n" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + \
                                                                  "---history : " + choice + "---" + str(current_layer['num']) + "---cost: " +\
                                                                  str(current_layer['price'] * int(buy_num)) + \
                                                                  old_history[old_history.index('\n',old_history.index(username+'_cash'))+1 :]
                                                with open("user_info.txt", mode="w",encoding="utf-8") as f:
                                                    f.write(new_history)
                                                current_layer = product_list  # 将当前层重置,已购商品数量会保留，字典为可变数据类型
                                            else:  # 用户余额不足时
                                                count_layer = 0  # 将层级数重置
                                                print("\nThe product price is " +
                                                      str(current_layer['price'])+ "*" +
                                                           buy_num + "! Your still need " +
                                                           str( current_layer['price'] * int(buy_num) - cash))
                                                recharge_choice = input(
                                                    "\nYou can input 'RE' to recharge or 'Q' to quit !")
                                                if recharge_choice.lower() == 're':  # 用户选择充值
                                                    recharge_num = input(
                                                        "\nPlease input the number you want to recharge : ")
                                                    cash += int(recharge_num)
                                                    print(
                                                        "\nRecharge Successful ! Now your cash is " + str(cash) + "\n")
                                                    current_layer = product_list  # 将商品字典充值
                                                    continue
                                                elif recharge_choice.lower() == 'q':  # 用户选择退出
                                                    f.close()  # 首先关闭打开的文件，准备后面更新文件信息
                                                    print("Your Bill :\n名称\t数量")  # 输出用户本次购物信息
                                                    for i in bill:
                                                        print(i)
                                                    print("Total Cost : " + str(total_cost))
                                                    print("Balance : " + str(cash))
                                                    print("\nLooking forward to your next visit !!!")
                                                    with open("user_info.txt", mode="r",
                                                              encoding="utf-8") as f:  # 更新文件中的cash
                                                        old_info = f.read()
                                                        new_info = old_info.replace(
                                                            (old_info[old_info.index(username + '_cash',
                                                                                     old_info.index(username))
                                                            :old_info.index('\n', old_info.index(username + '_cash'))]),
                                                            (username + '_cash:' + str(cash) + '\n'))
                                                    with open("user_info.txt", mode="w",
                                                              encoding="utf-8") as f:  # 写入新的cash余额
                                                        f.write(new_info)
                                                    exit()
                                        if not buy_num.isdigit():
                                            print("请输入数字！")

                                    elif is_buy.lower() == 'b':  # 用户返回上一层商品字典
                                        if last_layer:
                                            if count_layer > 0:  # 将层数减1
                                                count_layer -= 1
                                            current_layer = last_layer[len(last_layer) - 1]
                                            last_layer.pop()
                                            continue  # 跳出本次循环，用户进入上一层继续选择商品字典
                                    elif is_buy.lower() == 'q':  # 用户退出前显示当次购物信息
                                        f.close()
                                        print("Your Bill :\nCategory\t\tQuantity")
                                        for i in bill:
                                            print(i)
                                        print("Total Cost : " + str(total_cost))
                                        print("Balance : " + str(cash))
                                        print("\nLooking forward to your next visit !!!")
                                        # 更新cash余额,读取历史user_info信息
                                        with open("user_info.txt", mode="r", encoding="utf-8") as f:  # 更新文件中的cash
                                            old_info = f.read()
                                            new_info = old_info.replace(
                                                (old_info[old_info.index(username + '_cash', old_info.index(username))
                                                :old_info.index('\n', old_info.index(username + '_cash'))]),
                                                (username + '_cash:' + str(cash) + '\n'))
                                        with open("user_info.txt", mode="w", encoding="utf-8") as f:  # 写入新的cash余额
                                            f.write(new_info)
                                        exit()
                        elif count >= 3:  # 判断如果输入错误次数大于3次，则将用户加入至锁定名单
                            with open("user_locked.txt", mode="a", encoding="utf-8") as f_locked:
                                f_locked.write("\nusername:" + username)
                                print(
                                    "Sorry, you've try more than 3 times , "
                                    "this username will be added in locked_list , "
                                    "please contact Administrator !")
                                exit()
                        elif count < 3:
                            l_flag = False
                            count += 1  # 计数器，若count加至3，则用户尝试登陆次数过多，强制返回选择界面！
                            print("Incorrect username or password !")
                            break  # 退出循环，用户重新输入用户名和密码

                            # 用户注册功能
    if choice.lower() == "r":
        while True:
            new_username = input("Input new username (or 'Q' for exit):").strip()
            if new_username.lower() == "q":
                exit()
            new_password = getpass.getpass("Input new password (or 'Q' for exit):").strip()
            if new_password.lower() == "q":
                exit()
            with open("user_info.txt", mode="r+", encoding="utf-8") as f:
                f.seek(0)  # 光标重置至开头
                for line in f:
                    if line.startswith("username:") and new_username in line:  # 判断用户名是否已经存在，存在则不能注册
                        print("Sorry ! This username is already exist , please change !")
                        r_flag = True
                        break  # 用户名已经存在，不能注册，跳出循环重新输入
                if r_flag:  # 如果用户输入的用户名已经存在，则退出重新输入用户名，此处为注册标志位，退出本次循环
                    r_flag = False  # 注册标志重置
                    continue
                f.write("\nusername:" + new_username)
                f.write("\npassword:" + new_password)
                f.write("\n" + new_username + "_cash:" + str(0) + "\n")
                print("Congratulation ! " + new_username + " Register Successful !")
                break  # 用户注册成功，返回用户选择界面，用户可以选择登陆、继续注册或退出
                # 用户退出功能
    if choice.lower() == "q":
        exit()  # 用户退出
