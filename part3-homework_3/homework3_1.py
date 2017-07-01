# /usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "Elijah"
__date__ = "2017/6/24 20:28"

# ATM
# √ 1. 指定最大透支额度
# √ 2. 可取款
# √ 3. 定期还款（每月指定日期还款，如15号）
# √ 4. 可存款
# √ 5. 定期出账单
# √ 6. 支持多用户登陆，用户间转帐
# √ 7. 支持多用户
# √ 8. 管理员可添加账户、指定用户额度、冻结用户等

# 导入
import datetime
import re

# 全局变量
global_var = {'user_info': {},
              'user_name': '',
              'user_locked': [],
              'user_bill': [],
              'opera_num': '', }


# 函数定义
def login():
    '''
    功能选择界面
    :return:
    '''
    welcome_str = '''
                                      欢迎来到ATM自动取款机
------------------------------------------------------------------------------------------------------
请选择您的操作：
1、用户登陆
2、管理员登陆
3、退出
    '''
    while True:
        print(welcome_str)
        opera_num = input('请输入操作编号1-3：\n>>>').strip()
        if opera_num.isdigit() and 0 < int(opera_num) < 4:
            return opera_num
        else:
            print('你输入的操作编号有误！请重新输入！')
            continue


def read_info(user_info):
    '''
    将用户信息读至内存
    :return:info_dict
    '''
    info_list = []
    info_dict = {}
    with open(user_info, mode='r', encoding='utf-8') as f:
        for line in f:
            info_list.clear()
            # 密码
            info_list.append(line.split(',')[1])
            # 余额
            info_list.append(line.split(',')[2])
            # 额度
            info_list.append(line.split(',')[3])
            # 欠款
            info_list.append(line.split(',')[4])
            # 用户名为字典key
            info_dict[line.split(',')[0]] = info_list.copy()
        return info_dict


def write_info(info_dict, user_info):
    '''
    将内存写至用户文件
    :param info_dict:
    :param user_info:
    :return:
    '''
    with open(user_info, mode='w', encoding='utf-8') as f:
        for k, v in info_dict.items():
            f.write(k + ',' + v[0] + ',' + v[1] + ',' + v[2] + ',' + v[3] + ',\n')


def read_ubill(username):
    '''
    将用户账单读取到内存
    :param username:
    :return:
    '''
    bill_name = username + '_bill.txt'
    bill_list = []
    with open(bill_name, mode='r', encoding='utf-8') as f:
        bill_list.clear()
        for line in f:
            # 日期
            bill_list.append(line.split(',')[0])
            # 存款
            bill_list.append(line.split(',')[1])
            # 取款
            bill_list.append(line.split(',')[2])
            # 余额
            bill_list.append(line.split(',')[3])
        return bill_list


def write_ubill(bill_list, username):
    '''
    将用户账单写回文件
    :param bill_list:
    :param username:
    :return:
    '''
    str = ''
    bill_name = username + '_bill.txt'
    with open(bill_name, mode='w', encoding='utf-8') as f:
        for index, i in enumerate(bill_list):
            if (index + 1) % 4 == 0:
                str = str + i + ',\n'
            else:
                str = str + i + ','
        f.write(str)


def read_locked(user_locked):
    '''
    将锁定用户读至内存
    :param user_locked:
    :return:
    '''
    with open(user_locked, mode='r', encoding='utf-8') as f:
        locked = f.read()
        locked_list = locked.split(',')
        return locked_list


def write_locked(locked_list):
    '''
    将内存写至锁定用户文件
    :return:
    '''
    str = ''
    with open('user_locked.txt', mode='w', encoding='utf-8') as f_lock:
        for i in locked_list:
            str = str + i + ','
        f_lock.write(str)


def user_operation(info_dict, locked_list):
    '''
    用户操作
    :param info_dict:
    :param locked_list:
    :return: choice_num
    '''
    count = 0
    flag = False
    while True:
        username = input('请输入用户名(或者输入q退出):\n>>>').strip()
        if username.lower() == 'q':
            return ('6 , ')
        password = input('请输入密码:\n>>>').strip()
        # 判断用户名是否被冻结
        if username in locked_list:
            print('对不起，您输入的用户名已经被冻结，请联系管理员！')
            continue
        for k, v in info_dict.items():
            if k == username and v[0] == password:
                welcome_str = '''
            欢迎来到ATM自动取款机
-----------------------------------------------
1、存款
2、取款
3、转账
4、显示账单
5、修改密码
6、退出
                '''
                print(welcome_str)
                while True:
                    choice_num = input('\n请输入操作编号1-6：\n>>>').strip()
                    if choice_num.isdigit() and 0 < int(choice_num) < 7:
                        return (choice_num + ',' + username)
                    else:
                        print('对不起，您输入的操作编号有误，请重新输入！')
                        continue
            else:
                continue
        if flag:
            break
        count += 1
        if count > 3:
            if username in info_dict.keys():
                locked_list.append(username)
                print('对不起，您登陆失败的次数过多，该用户已经被冻结！')
                continue
        else:
            print('对不起，您输入的用户名或密码有误，请重新输入！')
            continue


def is_debt(info_dict, bill_list, username):
    '''
    检查用户是否有欠款
    :param info_dict:
    :param bill_list:
    :param username:
    :return:
    '''
    if (int(str(datetime.date.today()).split('-')[2]) == 1) and (int(info_dict[username][3]) > 0):
        if (int(info_dict[username][1]) - int(info_dict[username][3])) >= 0:
            debt_num = info_dict[username][3]
            info_dict[username][1] = str(int(info_dict[username][1]) - int(info_dict[username][3]))
            info_dict[username][3] = '0'
            # 将记录写入用户账单内存
            bill_list.append(str(datetime.date.today()))
            bill_list.append('0')
            bill_list.append(debt_num)
            bill_list.append(info_dict[username][1])
            print('您好，今天的日期是' + str(datetime.date.today()) + ',今日为还款日，系统已经自动为您还款！' +
                  '目前您的余额为：' + info_dict[username][1])
        else:
            print('您好，今天的日期是' + str(datetime.date.today()) +
                  ',今日为还款日，您的余额不足以还清欠款！请及时存款还款！\n目前您的余额为：' + info_dict[username][1])
    elif (int(str(datetime.date.today()).split('-')[2]) < 15) and (int(info_dict[username][3]) > 0):
        print('您好，今天的日期是' + str(datetime.date.today()) + '\n您目前欠款金额为：' + info_dict[username][3] +
              ',\n请在本月15日前还清欠款，否则系统将自动还款！')


def admin_operation():
    '''
    管理员操作：默认管理员用户名：admin，密码：admin123
    :return:
    '''
    while True:
        username = input('请输入管理员用户名，默认admin,(或者输入q退出):\n>>>').strip()
        if username.lower() == 'q':
            break
        password = input('请输入管理员密码，默认admin123:\n>>>').strip()
        if username == 'admin' and password == 'admin123':
            welcome_str = '''
    欢迎来到ATM自动取款机-管理员功能区
-----------------------------------------------
1、添加用户
2、冻结用户
3、设定用户额度
4、退出
            '''
            print(welcome_str)
            while True:
                choice_num = input('\n请输入操作编号1-4：\n>>>').strip()
                if choice_num.isdigit() and 0 < int(choice_num) < 5:
                    return choice_num
                else:
                    print('对不起，您输入的操作编号有误，请重新输入！')
                    continue
        else:
            continue


def deposit_money(info_dict, bill_list, username):
    '''
    存款
    :param info_dict:
    :return:
    '''
    while True:
        deposit_num = input('请输入存款金额(或者输入q退出)：\n>>>').strip()
        if deposit_num.isdigit():
            print('当前余额为：' + info_dict[username][1] + '\n存入后余额为：' + str(int(info_dict[username][1]) + int(deposit_num)))
            is_sure = input('是否确认存款(y/n)?\n>>>').strip()
            if is_sure.lower() == 'y':
                # 将用户字典余额刷新至内存
                info_dict[username][1] = str(int(info_dict[username][1]) + int(deposit_num))
                # 将记录写入用户账单内存
                bill_list.append(str(datetime.date.today()))
                bill_list.append(deposit_num)
                bill_list.append('0')
                bill_list.append(info_dict[username][1])
            elif is_sure.lower() == 'n':
                break
            else:
                print('输入有误，请重新确认！')
                continue
        elif deposit_num.lower() == 'q':
            break
        else:
            print('存款金额输入有误，请重新输入！')
            continue


def draw_money(info_dict, bill_list, username):
    '''
    取款
    :return:
    '''
    while True:
        draw_num = input('请输入取款金额(或者输入q退出)：\n>>>').strip()
        if draw_num.isdigit() and ((int(info_dict[username][1]) + int(info_dict[username][2]) - int(draw_num)) >= 0):
            print('当前余额为：' + info_dict[username][1] + '\n取款后后余额为：' + str(int(info_dict[username][1]) - int(draw_num)))
            is_sure = input('是否确认取款(y/n)?\n>>>').strip()
            if is_sure.lower() == 'y':
                # 将用户字典余额刷新至内存-余额不足情况
                if (int(info_dict[username][1]) < int(draw_num) < (
                            int(info_dict[username][1]) + int(info_dict[username][3]))):
                    info_dict[username][1] = '0'
                    info_dict[username][3] = str(int(draw_num) - int(info_dict[username][1]))
                    # 将记录写入用户账单内存
                    bill_list.append(str(datetime.date.today()))
                    bill_list.append('0')
                    bill_list.append(draw_num)
                    bill_list.append('0')
                # 将用户字典余额刷新至内存-余额足够情况
                elif (int(info_dict[username][1]) >= int(draw_num)):
                    info_dict[username][1] = str(int(info_dict[username][1]) - int(draw_num))
                    # 将记录写入用户账单内存
                    bill_list.append(str(datetime.date.today()))
                    bill_list.append('0')
                    bill_list.append(draw_num)
                    bill_list.append(str(int(info_dict[username][1])))
            elif is_sure.lower() == 'n':
                break
            else:
                print('输入有误，请重新确认！\n')
                continue
        elif draw_num.lower() == 'q':
            break
        elif draw_num.isdigit() and ((int(info_dict[username][1]) + int(info_dict[username][2] - int(draw_num))) < 0):
            print('对不起，取款金额大于当前余额与最大额度之和，请重新输入！\n用户：' + username +
                  ' 当前余额为：' + info_dict[username][1] + '\n')
            continue
        else:
            print('取款金额输入有误，请重新输入！\n')
            continue


def trans_money(info_dict, bill_list, username):
    '''
    转账
    :param info_dict:
    :param bill_list:
    :param username:
    :return:
    '''
    while True:
        for index, i in enumerate(info_dict.keys()):
            if not i == username:
                if (index + 1) % 5 == 0:
                    print(str(i) + '\n', end='')
                else:
                    print(str(i) + '、', end='')
        trans_choice = input('\n请输入向哪位用户转账(或者输入q退出)：\n>>>').strip()
        if trans_choice in info_dict.keys():
            trans_num = input('请输入转账金额:\n>>>').strip()
            if (trans_num.isdigit()) and (int(trans_num) <= int(info_dict[username][2])):
                is_sure = input('是否确定向用户 ' + trans_choice + ' 转账：' + trans_num + ' ? (y/n)\n>>>')
                if is_sure.lower() == 'y':
                    # 将双方用户字典余额刷新至内存
                    info_dict[trans_choice][1] = str(int(info_dict[trans_choice][1]) + int(trans_num))
                    info_dict[username][1] = str(int(info_dict[username][1]) - int(trans_num))
                    # 将记录写入此用户账单内存
                    bill_list.append(str(datetime.date.today()))
                    bill_list.append('0')
                    bill_list.append(trans_num)
                    bill_list.append(str(int(info_dict[username][1])))
                    # 将记录写入对方用户账单文件
                    trans_name = trans_choice + '_bill.txt'
                    with open(trans_name, mode='w', encoding='utf-8') as f:
                        f.write(str(datetime.date.today()) + ',' + trans_num + ',' + '0' + ',' + str(
                            info_dict[trans_choice][1]) + ',')
                    print('转账成功！')
                elif is_sure.lower() == 'n':
                    continue
                else:
                    print('输入有误，请重新输入！\n')
                    continue
            else:
                print('对不起，您输入的金额有误或超出现有余额，请重新输入！\n')
                continue
        elif trans_choice.lower() == 'q':
            break
        else:
            print('对不起，你输入的用户名有误，请重新输入！\n')
            continue


def show_bill(username):
    '''
    显示账单
    :return:
    '''
    while True:
        choice_bill = input('\n请输入查询的账单年月,如2017-05(或者输入q退出)：\n>>>').strip()
        if re.match(r"^[0-9]{6}", choice_bill.replace('-', '')):
            print(choice_bill.rjust(15, '-') + ' ' + '用户:' + username + ' 账单明细'.ljust(15, '-'))
            print('交易日期 | 存款金额 | 取款金额 | 余额')
            bill_name = username + '_bill.txt'
            with open(bill_name, mode='r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith(choice_bill):
                        print(line.replace(',', '     '), end="")
        elif choice_bill.lower() == 'q':
            break
        else:
            print('对不起，您输入的查询账单年月有误，请重新输入！')
            continue


def change_pwd(info_dict, username):
    '''
    修改用户密码
    :return:
    '''
    flag = False
    while True:
        for k, v in info_dict.items():
            if k == username:
                old_pwd = input('请输入用户 ' + username + '原密码：\n>>>').strip()
                if old_pwd == v[0]:
                    new_pwd = input('请输入新密码：\n>>>').strip()
                    v[0] = new_pwd
                    print('密码修改成功！')
                    flag = True
                    break
                else:
                    print('对不起，您输入的原密码不正确，请重新输入！')
                    break
            else:
                continue
        if flag:
            break


def add_user(info_dict):
    '''
    添加用户
    :return:
    '''
    new_list = []
    while True:
        new_user = input('请输入想要添加的用户名(或者输入q退出)：\n>>>').strip()
        if new_user.lower() == 'q':
            break
        if new_user in info_dict.keys():
            print('对不起，此用户名已经存在！请重新输入！')
            continue
        else:
            new_pwd = input('请设置用户 ' + new_user + '密码：\n>>>').strip()
            new_list.append(new_pwd)
            new_list.append('0')
            new_list.append('10000')
            new_list.append('0')
            info_dict[new_user] = new_list.copy()
            print('用户 ' + new_user + '添加成功！默认用户额度为10000！')


def freeze_user(info_dict, locked_list):
    '''
    冻结用户
    :param info_dict:
    :param locked_list:
    :return:
    '''
    while True:
        user_lock = input('请输入要冻结的用户名(或者输入q退出):\n>>>').strip()
        if user_lock in info_dict.keys():
            is_sure = input('确认要冻结用户 ' + user_lock + ' ? (y/n)').strip()
            if is_sure.lower() == 'y':
                locked_list.append(user_lock)
            elif is_sure.lower() == 'n':
                break
            else:
                print('您的输入有误，请重新输入！')
                continue
        elif user_lock.lower() == 'q':
            break
        else:
            print('对不起，您输入的用户名不存在，请重新输入！')
            continue


def set_limit(info_dict):
    '''
    指定用户额度
    :return:
    '''

    flag = False
    while True:
        choice_user = input('请输入想要修改密码的用户名(或者输入q退出)：\n>>>').strip()
        if choice_user.lower() == 'q':
            break
        for k, v in info_dict.items():
            if k == choice_user:
                old_pwd = input('请输入用户 ' + choice_user + '密码：\n>>>').strip()
                if old_pwd == v[0]:
                    new_limit = input('请输入用户新额度：\n>>>').strip()
                    v[2] = new_limit
                    print('用户额度修改成功！')
                    flag = True
                    break
                else:
                    print('对不起，您输入的原密码不正确，请重新输入！')
                    break
            else:
                continue
        if flag:
            break


# 主函数
if __name__ == '__main__':
    while True:
        # 将用户信息内容取到全局变量
        global_var['user_info'] = read_info('user_info.txt')
        global_var['user_locked'] = read_locked('user_locked.txt')
        # 选择用户/管理员登陆
        login_choice = login()
        if login_choice.strip() == '1':
            opera_return = user_operation(global_var['user_info'], global_var['user_locked'])
            write_locked(global_var['user_locked'])
            write_info(global_var['user_info'], 'user_info.txt')
            global_var['opera_num'] = opera_return.split(',')[0]
            global_var['user_name'] = opera_return.split(',')[1]
            try:
                global_var['user_bill'] = read_ubill(global_var['user_name'])
            except:
                with open((global_var['user_name'] + '_bill.txt'), mode='w', encoding='utf-8') as f:
                    f.write('')

            # 用户-存款
            if global_var['opera_num'].strip() == '1':
                deposit_money(global_var['user_info'], global_var['user_bill'], global_var['user_name'])
                write_info(global_var['user_info'], 'user_info.txt')
                write_ubill(global_var['user_bill'], global_var['user_name'])
                write_locked(global_var['user_locked'])
            # 用户-取款
            elif global_var['opera_num'].strip() == '2':
                is_debt(global_var['user_info'], global_var['user_bill'], global_var['user_name'])
                draw_money(global_var['user_info'], global_var['user_bill'], global_var['user_name'])
                write_info(global_var['user_info'], 'user_info.txt')
                write_ubill(global_var['user_bill'], global_var['user_name'])
                # write_locked(global_var['user_locked'])
            # 用户-转账
            elif global_var['opera_num'].strip() == '3':
                trans_money(global_var['user_info'], global_var['user_bill'], global_var['user_name'])
                write_info(global_var['user_info'], 'user_info.txt')
                write_ubill(global_var['user_bill'], global_var['user_name'])
                write_locked(global_var['user_locked'])
            # 用户-显示账单
            elif global_var['opera_num'].strip() == '4':
                show_bill(global_var['user_name'])
            # 用户-修改密码
            elif global_var['opera_num'].strip() == '5':
                change_pwd(global_var['user_info'], global_var['user_name'])
                write_info(global_var['user_info'], 'user_info.txt')
            # 用户-退出
            elif global_var['opera_num'].strip() == '6':
                print('欢迎您下次光临ATM自动取款机！再见！')
                exit()
        elif login_choice.strip() == '2':
            # 添加用户
            admin_choice = admin_operation()
            if admin_choice.strip() == '1':
                add_user(global_var['user_info'])
                write_info(global_var['user_info'], 'user_info.txt')
            # 冻结用户
            elif admin_choice.strip() == '2':
                freeze_user(global_var['user_info'], global_var['user_locked'])
                write_locked(global_var['user_locked'])
            # 设定用户额度
            elif admin_choice.strip() == '3':
                set_limit(global_var['user_info'])
                write_info(global_var['user_info'], 'user_info.txt')
            # 退出
            elif admin_choice.strip() == '4':
                print('管理程序退出！谢谢光临！')
                exit()
        elif login_choice.strip() == '3':
            print('欢迎您下次光临ATM自动取款机！再见！')
            exit()
        else:
            print('您的输入有误，请重新输入！')
            continue
