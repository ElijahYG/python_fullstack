# -*- coding:utf-8 -*-

# Readme
# Author: Elijah
# Time: 2017-06-07
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
# Important py file：getpass,time
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
                '2匹柜式空调': {'price': 4000, 'num': 0, 'sum': 10},
                '3匹柜式空调': {'price': 6000, 'num': 0, 'sum': 10},
            },
        },
    },
}

# 用于分级显示
current_layer = product_list
last_layer = [product_list]

# 用户存储用户购物信息，用户购物结束输出
bill = []

# 标志位、计数器
r_flag = False
l_flag = False
op_flag = False
shop_flag = False
count = 0
count_layer = 0
total_cost = 0

#全局变量
gl_user_info = ''
gl_user_locked = ''
username = ''
password = ''

while not op_flag:
    # 用户选择界面，可以进行注册、登陆和退出
    choice = input("Input 'R(Register)' to Register \nInput 'L(login)' to Login \nInput 'Q(quit)' to Quit \n>>>")
    # 用户登陆功能
    if choice.lower() == "l":
        while not l_flag:
            username = input("Input your username (or 'Q' for exit):").strip()
            if username.lower() == "q":
                op_flag = True
                print("end".center(40, "-"))
                break
            password = input("Input your password (or 'Q' for exit):").strip()
            if password.lower() == "q":
                op_flag = True
                print("end".center(40, "-"))
                break
            # 判断用户是否在锁定名单中
            with open("user_locked.txt", mode="r", encoding="utf-8") as f_locked:
                gl_user_locked = f_locked.read()
                f_locked.close()
                if username in gl_user_locked:
                    print("This username has been locked , please contact Administrator !\n")
                    break
            with open("user_info.txt", mode="r", encoding="utf-8") as f:
                # 校验账户
                gl_user_info = f.read()
                f.close()
                if (("username:%s\npassword:%s")%(username,password)) in gl_user_info:
                    #登陆成功，进入购物车功能
                    op_flag = True
                    break
                # 判断如果输入错误次数大于3次，则将用户加入至锁定名单
                elif count >= 3:
                    gl_user_locked = gl_user_locked + username + "\n"
                    with open("user_locked.txt", mode="a", encoding="utf-8") as f_locked:
                        f_locked.write(gl_user_locked)
                        print(
                            "Sorry, you've try more than 3 times ,this username will be added in locked_list , "
                            "please contact Administrator !\n")
                        exit()
                else:
                    count += 1
                    print(" Incorrect username or password ! Please ensure you have Account ! "
                          "You can retry and input 'R' to register .\n")
                    break
    # 用户注册功能
    if choice.lower() == "r":
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
                    # 判断用户名是否已经存在，存在则不能注册
                    if line.startswith("username:") and new_username in line:
                        print("Sorry ! This username is already exist , please change !")
                        r_flag = True
                        break
                # 如果用户输入的用户名已经存在，则退出重新输入用户名
                if r_flag:
                    r_flag = False
                    continue
                # 用户注册成功，返回用户选择界面，用户可以选择登陆、继续注册或退出
                f.write("username:" + new_username + "\n")
                f.write("password:" + new_password + "\n")
                f.write(new_username + "_cash:" + str(0) + "\n")
                print("Congratulation ! " + new_username + " Register Successful !\n")
                break
    # 用户退出功能
    if choice.lower() == "q":
        exit()
    else:
        continue

#登陆购物车成功，输出历史购物信息
print("Welcome " + username + " ! " + " Login Successful !")
cash = int(
    gl_user_info[gl_user_info.find(username+"_cash:"):gl_user_info.find("\n",gl_user_info.find(username+"_cash:"))].split(":")[1].strip())
Consup_hist = gl_user_info
Consup_hist = Consup_hist[Consup_hist.find('\n', Consup_hist.find(username + '_cash')):
Consup_hist.find('username', Consup_hist.find(username + '_cash'))]
print("\nConsumption history below：" + "\n" + Consup_hist)
Consup_hist = ''
print("\nYour Balance is :" + str(cash))
if cash == 0:
    cash = int(input("Please input your available cash:").strip())
while not shop_flag:
    # 商品字典有4级，用计数器控制进入字典的层级数
    if count_layer <= 3:
        print("\n目前是第" + str(count_layer + 1) + "层商品目录")
        for key in current_layer:
            print(key)
        choice = input("Input the Product Name you want to buy or input 'B' to back or input 'Q' to quit\n>>>").strip()
        if choice in current_layer:
            last_layer.append(current_layer)
            current_layer = current_layer[choice]
            count_layer += 1
        if choice.lower() == 'b':
            if last_layer:
                if count_layer > 0:
                    count_layer -= 1
                current_layer = last_layer[len(last_layer) - 1]
                last_layer.pop()
                continue
        # 用户选择退出
        if choice.lower() == 'q':
            shop_flag = True
            break
    # 进入最后一层商品目录，显示单价和数量，提问用户选择是否购买
    else:
        print('单价：' + str(current_layer['price'])+ "\n",
              '已购数量：' + str(current_layer['num'])+ "\n",
              '库存数量：' + str(current_layer['sum'])+ "\n",
              )
        is_buy = input("If you decided to buy ,please input 'Y' or input 'B'to back or 'Q' to quit\n>>>").strip()
        # 用户确认购买
        if is_buy.lower() == 'y':
            buy_num = input("Please input the Number you want to buy :\n>>>").strip()
            if buy_num.isdigit():
                if cash >= current_layer['price'] * int(buy_num):
                    count_layer = 0
                    cash -= current_layer['price'] * int(buy_num)
                    if (current_layer['sum'] <= 0) or (int(buy_num) > current_layer['sum']):
                        count_layer = 0
                        current_layer = last_layer[0]
                        last_layer.clear()
                        print("对不起！库存不足，请重新选择\nSorry！ Insufficient stock ！")
                        continue
                    else:
                        current_layer['sum'] -= int(buy_num)
                    current_layer['num'] += int(buy_num)
                    print("Added " + str(buy_num) + " * " + choice +
                          " into shopping cart ! Now your current cash is " +
                          str(cash) + "\n")
                    bill.append([choice, int(buy_num)])
                    total_cost += current_layer['price'] * int(buy_num)
                    # 更新购物信息
                    gl_user_info = gl_user_info[0:gl_user_info.index('\n', gl_user_info.index(username + '_cash'))] + \
                                  "\n" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + \
                                  "---history : " + choice + "---" + buy_num + "---cost: " + \
                                  str(current_layer['price'] * int(buy_num)) + "\n"+ \
                                  gl_user_info[gl_user_info.index('\n', gl_user_info.index(username + '_cash')) + 1:]
                    current_layer = product_list
                # 用户余额不足
                else:
                    count_layer = 0
                    print("The product price is " + str(current_layer['price']) + "*" + buy_num +
                          "! Your still need " + str(current_layer['price'] * int(buy_num) - cash) + "\n")
                    recharge_choice = input( "You can input 'RE' to recharge or 'Q' to quit !\n>>>").strip()
                    # 用户选择充值
                    if recharge_choice.lower() == 're':
                        recharge_num = input("Please input the Number you want to recharge : \n>>>").strip()
                        if recharge_num.isdigit():
                            cash += int(recharge_num)
                        if not recharge_num.isdigit():
                            count_layer = 0
                            current_layer = last_layer[0]
                            last_layer.clear()
                            print("Please input digit ！")
                            continue
                        print( "Recharge Successful ! Now your cash is " + str(cash) + "\n")
                        current_layer = product_list
                        continue
                    # 用户选择退出
                    elif recharge_choice.lower() == 'q':
                        shop_flag = True
                        break
                    else:
                        count_layer = 0
                        current_layer = last_layer[0]
                        last_layer.clear()
                        print("Entered incorrectly ! Please Reselection !")
                        continue
            if not buy_num.isdigit():
                print("请输入数字！")
        # 用户返回上一层商品字典
        elif is_buy.lower() == 'b':
            if last_layer:
                if count_layer > 0:
                    count_layer -= 1
                current_layer = last_layer[len(last_layer) - 1]
                last_layer.pop()
                continue
        # 用户退出前显示当次购物信息
        elif is_buy.lower() == 'q':
            shop_flag = True
            break
#用户退出，输入本次购物信息并保存
print("Your Bill :\n名称\t数量\n" + "----"*10)
for i in bill:
    print(i)
print("Total Cost : " + str(total_cost))
print("Balance : " + str(cash) + "\n" + "----"*10)
print("Looking forward to your next visit !!!")
gl_user_info = gl_user_info.replace(
    (gl_user_info[gl_user_info.index(username + '_cash', gl_user_info.index(username))
    :gl_user_info.index('\n', gl_user_info.index(username + '_cash'))]),(username + '_cash:' + str(cash) + '\n'))
with open("user_info.txt", mode="w", encoding="utf-8") as f:
    f.write(gl_user_info)
exit()