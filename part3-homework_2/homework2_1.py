#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "Elijah"
__date__ = "2017/6/20 23:26"

# Readme
# Author: Elijah
# Time: 2017-06-20
# Function:员工信息表程序
#     可进行模糊查询，语法至少支持下面3种:
#         select name,age from staff_table where age > 22
#         select  * from staff_table where dept = "IT"
#         select  * from staff_table where enroll_date like "2013"
#     查到的信息，打印后，最后面还要显示查到的条数
#     可创建新员工纪录，以phone做唯一键，staff_id需自增
#     可删除指定员工信息纪录，输入员工id，即可删除
#     可修改员工信息，语法如下:
#       UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
#     1. 支持至少三种方法的select查询，并在最后显示查询到的条数。
#     2. 创建新员工记录，以phone为唯一键，staff_id自增
#     3. 输入员工id可删除指定员工信息记录
#     4. 可以使用UPDATE命令修改指定员工信息。
# Need Environment：Python 3.5 、PyCharm
# Move：
# Feature：
# Important py file：re、time
# How To：Execute directly
# 个人发挥：用模块化的编程思想
# 个人博客地址：http://blog.csdn.net/dragonyangang/article/details/74069329

# 导入
import re
import time

# 全局变量
global_staffdict = {}


# 函数定义
def operation():
    '''
    功能选择界面
    :param :
    :return: opera_num
    '''
    welcome_str = '''
                                      欢迎来到员工信息查询程序
------------------------------------------------------------------------------------------------------
操作语法说明：

添加：insert into TABLE_NAME where NAME,AGE,PHONE,DEPT,ENROLL_DATE,
删除：delete ID
修改：update TABLE_NAME set FIELD = 'NEW_VALUE' where FIELD = 'OLD_VALUE'
查询：select FIELD1, FIELD2... from TABLE_NAME where FIELD1 = 'CONDITION'
      select * from TABLE_NAME where FIELD = 'CONDITION'
      select * from TABLE_NAME where FIELD like 'CONDITION'

特别说明：
目前默认的员工信息表TABLE_NAME为:staff_table
查询：条件有且只能有一个，并且所有字段和符号间要加空格，查询条件要加引号
修改：修改是set字段与where条件字段必须一致
------------------------------------------------------------------------------------------------------
请选择您的操作：
1、添加新员工信息
2、删除员工信息
3、修改员工信息
4、查询员工信息
5、退出程序
    '''
    print(welcome_str)
    opera_num = input('请输入操作编号1-5：\n>>>').strip()
    return opera_num


def read_table():
    '''
    将SQL表文件读取至内存
    :param :
    :return:staff_dict
    '''
    staff_dict = {}
    staff_list = []
    with open('staff_table.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            staff_list.clear()
            staff_list.append(line.split(',')[1])
            staff_list.append(line.split(',')[2])
            staff_list.append(line.split(',')[3])
            staff_list.append(line.split(',')[4])
            staff_list.append(line.split(',')[5])
            staff_dict[line.split(',')[0]] = staff_list.copy()
    return staff_dict


def write_table(staff_dict):
    '''
    将内存数据写至SQL表文件
    :param staff_dict:
    :return:
    '''
    with open('staff_table.txt', mode='w', encoding='utf-8') as f:
        for k, v in staff_dict.items():
            f.write(str(k) + ',' + v[0] + ',' + v[1] + ',' + v[2] + ',' + v[3] + ',' + v[4] + ',\n')


def creat(staff_dict):
    '''
    添加员工信息
    :param :staff_dict
    :return:None
    '''
    while True:
        loop_flag = False
        staff_list = []
        print(
            '添加语法说明：\ninsert into TABLE_NAME where NAME,AGE,PHONE,DEPT,ENROLL_DATE(yyyy-mm-dd),字段中间不可有空格且ENROLL_DATE后有逗号')
        new_staff = input('请输入添加命令(或者输入q退出)：\n>>>').strip()
        if (new_staff.split('into')[0] == 'insert ') and (len(new_staff.split()) == 5):
            # 判断手机号是否重复
            for k, v in staff_dict.items():
                if new_staff.replace(',', ' ').split()[6] == v[2]:
                    print('对不起，您输入的手机号与下列记录重复!\n\t' + 'staff_id: ' + str(k) + str(v) + '\n请重新输入！\n')
                    loop_flag = True
                    break
                elif not re.match(r"^1[0-9]{10}$", new_staff.replace(',', ' ').split()[6]):
                    print('对不起，您输入的手机号有误，请重新输入！')
                    loop_flag = True
                    break
                elif not new_staff.replace(',', ' ').split()[5].isdigit():
                    print('对不起，您输入的年龄有误，请输入数字！')
                    loop_flag = True
                    break
                elif new_staff.replace(',', ', ').split()[8]:
                    try:
                        time.strptime(new_staff.replace(',', ' ').split()[8], "%Y-%m-%d")
                    except:
                        print('对不起，您输入的入职时间格式有误，请重新输入！正确格式例如：2017-06-20 ')
                        loop_flag = True
                        break
            if loop_flag:
                continue
            staff_list.append(new_staff.replace(',', ' ').split()[4])
            staff_list.append(new_staff.replace(',', ' ').split()[5])
            staff_list.append(new_staff.replace(',', ' ').split()[6])
            staff_list.append(new_staff.replace(',', ' ').split()[7])
            staff_list.append(new_staff.replace(',', ' ').split()[8])
            staff_dict[len(list(staff_dict.keys())) + 1] = staff_list
            print(staff_dict)
            print('员工信息添加成功！\n')
            break
        elif new_staff.lower() == 'q':
            break
        else:
            print('您输入的添加命令有误，请重新输入！'
                  '正确格式例如：insert into staff_table where A,20,13812345678,IT,2015-09-20')
            continue


def retrieve(staff_dict):
    '''
    查询员工信息
    :param :
    :return:
    '''
    while True:
        count = 0
        field_dict = {'name': 0, 'age': 1, 'phone': 2, 'dept': 3, 'enroll_date': 4}
        print('员工信息表staff_table结构说明'.center(50, "-"))
        print('| name | age | phone | dept | enroll_date |\n'.center(50, " "))
        print('查询语法说明：\nselect FIELD1,FIELD2... from TABLE_NAME where FIELD2=CONDITION(不支持多个条件查询);\n'
              'select * from TABLE_NAME where FIELD = CONDITION;\n'
              'select * from TABLE_NAME where FIELD like VALUE \n')
        retrieve_staff = input('请输入查询命令(或者输入q退出)：\n>>>').strip()
        if retrieve_staff.split()[0] == 'select' and '*' and 'like' in retrieve_staff:
            if len(retrieve_staff.split()) == 8:
                cmd_list = retrieve_staff.split()
            else:
                print("你输入的查询命令有误！请重新输入！"
                      "\n正确格式例如：select * from staff_table where name like 'Alex' 并且判断符号只能为：>、<、=")
                continue
            for k, v in staff_dict.items():
                try:
                    if cmd_list[7].split('\'')[1] in v[field_dict[cmd_list[5]]]:
                        show_info = '''staff_id: %s name: %s age: %s phone: %s dept: %s enroll_date: %s''' \
                                    % (k, v[0], v[1], v[2], v[3], v[4])
                        print(show_info)
                        count += 1
                    else:
                        continue
                except:
                    print("你输入的查询命令有误！请重新输入！"
                          "\n正确格式例如：select * from staff_table where name like 'Alex' 并且判断符号只能为：>、<、=")
                    break
            print('\n共查询出匹配条目 ' + str(count) + ' 项\n')
        elif retrieve_staff.split()[0] == 'select' and '*' in retrieve_staff:
            if len(retrieve_staff.split()) >= 8:
                cmd_list = retrieve_staff.split()
            else:
                print("你输入的查询命令有误！请重新输入！"
                      "\n正确格式例如：select * from staff_table where age > '36' 并且判断符号只能为：>、<、=")
                continue
            for k, v in staff_dict.items():
                if cmd_list[6] == '=' and v[field_dict[cmd_list[5]]] == cmd_list[7].split('\'')[1]:
                    show_info = '''staff_id: %s name: %s age: %s phone: %s dept: %s enroll_date: %s''' \
                                % (k, v[0], v[1], v[2], v[3], v[4])
                    print(show_info)
                    count += 1
                elif cmd_list[6] == '>' and v[field_dict[cmd_list[5]]] > cmd_list[7].split('\'')[1]:
                    show_info = '''staff_id: %s name: %s age: %s phone: %s dept: %s enroll_date: %s''' \
                                % (k, v[0], v[1], v[2], v[3], v[4])
                    print(show_info)
                    count += 1
                elif cmd_list[6] == '<' and v[field_dict[cmd_list[5]]] < cmd_list[7].split('\'')[1]:
                    show_info = '''staff_id: %s name: %s age: %s phone: %s dept: %s enroll_date: %s''' \
                                % (k, v[0], v[1], v[2], v[3], v[4])
                    print(show_info)
                    count += 1
                else:
                    continue
            print('\n共查询出匹配条目' + str(count) + '项\n')
        elif (retrieve_staff.split()[0] == 'select') and ('name' in retrieve_staff or 'age' in retrieve_staff
                                                          or 'phone' in retrieve_staff or 'dept' in retrieve_staff
                                                          or 'enroll_date' in retrieve_staff):
            select_fldlist = retrieve_staff[retrieve_staff.index(' '):retrieve_staff.index('from')].replace(' ',
                                                                                                            '').split(
                ',')
            select_cdtlist = retrieve_staff[retrieve_staff.index(' ', retrieve_staff.index('where')):].split()
            for k, v in staff_dict.items():
                if len(select_cdtlist) == 3:
                    if select_cdtlist[1] == '=' and v[field_dict[select_cdtlist[0]]] == select_cdtlist[2].split('\'')[
                        1]:
                        print('\nstaff_id: ' + k, end=" ")
                        for field in select_fldlist:
                            print(field + ': ' + v[field_dict[field]], end=" ")
                        count += 1
                    elif select_cdtlist[1] == '>' and v[field_dict[select_cdtlist[0]]] > select_cdtlist[2].split('\'')[
                        1]:
                        print('\nstaff_id: ' + k, end=" ")
                        for field in select_fldlist:
                            print(field + ': ' + v[field_dict[field]], end=" ")
                        count += 1
                    elif select_cdtlist[1] == '<' and v[field_dict[select_cdtlist[0]]] < select_cdtlist[2].split('\'')[
                        1]:
                        print('\nstaff_id: ' + k, end=" ")
                        for field in select_fldlist:
                            print(field + ': ' + v[field_dict[field]], end=" ")
                        count += 1
                    else:
                        continue
                else:
                    print("你输入的查询命令有误！请重新输入！"
                          "\n正确格式例如：select name,age,dept from staff_table where age > '35' 并且判断符号只能为：>、<、=")
                    continue
            print(print('\n共查询出匹配条目' + str(count) + '项\n'))
        elif retrieve_staff.lower() == 'q':
            break
        else:
            print('对不起，您输入的修改命令有误，请重新输入！')
            continue


def update(staff_dict):
    '''
    修改员工信息
    :param :staff_dict
    :return:
    '''
    while True:
        for k, v in staff_dict.items():
            show_info = '''staff_id: %s name: %s age: %s phone: %s dept: %s enroll_date: %s''' \
                        % (k, v[0], v[1], v[2], v[3], v[4])
            print(show_info)
        update_staff = input('\n请选择要修改的员工信息编号(或者输入q退出)：\n>>>').strip()
        if update_staff.isdigit() and 0 < int(update_staff) <= len(staff_dict):
            print("修改语法说明：\nupdate TABLE_NAME set FIELD='NEW VALUE' where FIELD='OLD VALUE' ")
            print('\n您选择修改的员工信息为：\n' + str(staff_dict[update_staff]))
            update_cmd = input('\n请输入修改命令(或者输入q退出)：\n>>>').strip()
            if update_cmd.split()[0] == 'update':
                try:
                    if update_cmd.split('\'')[3] in staff_dict[update_staff]:
                        # 找出旧值[3]在字典中的下标，之后将新值[1]写入
                        field_index = staff_dict[update_staff].index(update_cmd.split('\'')[3])
                        staff_dict[update_staff][field_index] = update_cmd.split('\'')[1]
                        print(staff_dict)
                        print('员工信息修改成功！')
                        break
                    else:
                        print('对不起，您输入的查询条件 ' + str(update_cmd.split('\'')[3]) +
                              ' 与记录\n' + str(staff_dict[update_staff]) + '\n不匹配，请重新输入！\n')
                        continue
                except:
                    print("修改命令中的字段值必须添加引号！请重新输入修改命令！"
                          "例如：update staff_table set age='66' where set='36'\n")
                    continue
            elif update_cmd.lower() == 'q':
                break
            else:
                print('对不起，您输入的修改命令有误，请重新输入！\n')
                continue
        elif update_staff.lower() == 'q':
            break
        else:
            print('请输入正确的编号！\n')
            continue


def delete(staff_dict):
    '''
    删除员工信息
    :param :staff_dict
    :return:
    '''
    while True:
        for k, v in staff_dict.items():
            show_info = '''staff_id: %s name: %s age: %s phone: %s dept: %s enroll_date: %s''' \
                        % (k, v[0], v[1], v[2], v[3], v[4])
            print(show_info)
        del_staff = input('\n请输入您要删除的编号staff_id(或者输入q退出):\n>>>').strip()
        if del_staff.isdigit() and 0 < int(del_staff) <= len(staff_dict):
            is_sure = input('请确认是否删除员工信息(y/n)：\n' + str(staff_dict[del_staff]) + '\n>>>').strip()
            if is_sure.lower() == 'y':
                del staff_dict[del_staff]
                print('员工信息删除成功！')
                break
            elif is_sure.lower() == 'n':
                break
            else:
                print('输入有误，请重新选择！\n')
                continue
        elif del_staff.lower() == 'q':
            break
        else:
            print('请输入正确的编号！\n')
            continue


# 主函数
if __name__ == '__main__':
    while True:
        # 将数据表内容取到内存
        global_staffdict = read_table()
        opera_num = operation()
        if opera_num.isdigit() and str(0) < opera_num < str(6):
            # 添加功能
            if opera_num == '1':
                creat(global_staffdict)
                write_table(global_staffdict)
                continue
            # 删除功能
            elif opera_num == '2':
                delete(global_staffdict)
                write_table(global_staffdict)
                continue
            # 修改功能
            elif opera_num == '3':
                update(global_staffdict)
                write_table(global_staffdict)
                continue
            # 查询功能
            elif opera_num == '4':
                retrieve(global_staffdict)
                write_table(global_staffdict)
                continue
            # 用户退出
            else:
                while True:
                    is_exit = input('是否确认退出（y/n）？\n>>>')
                    if is_exit.lower() == 'y':
                        write_table(global_staffdict)
                        exit()
                    elif is_exit.lower() == 'n':
                        break
                    else:
                        print('您输入的操作有误，请重新输入！')
                        continue
        else:
            print('对不起，您输入的操作编号有误，请重新输入！')
            continue
