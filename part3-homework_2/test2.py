# /usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "Elijah"
__date__ = "2017/6/21 13:55"
#
# import os           #导入os模块，方便文件的删除和改名
#
# def info_display():      #打印程序启动信息
#     print("-".center(60, "-"))
#     print("欢迎来到员工管理系统".center(50," "))
#     print("【输入help显示帮助信息】".center(50, " "))
#     print("-".center(60, "-"))
#     sql = input("请输入\033[1;31msql\033[0m信息>>>>").strip("")
#     if sql == "q" or sql == "quit":                #用户如果输入q，程序退出
#         exit(" Bye Bye ".center(60, "-"))
#     elif sql == "help":                            #用户输入help，打印help信息，help信息为打印的格式
#         print("\033[1;35m 查询 输入格式：\n\tselect name,age from staff_table where age > 22\033[0m")
#         print("\033[1;35m 创建 输入格式：\n\tinsert Mickle,22,13651054608,IT,2013-04-01\033[0m")
#         print("\033[1;35m 修改 输入格式：\n\tupdate staff_table set dept = \"Market\" where dept = \"IT\"\033[0m")
#         print("\033[1;35m 删除 输入格式：\n\tdelete 5\033[0m")
#     else:
#         sql_parse(sql)                              #用户输入正确的sql语法，调用sql解析函数
#
# def sql_parse(sql):                                #对用户输入的sql语句进行解析，根据sql语句调用不同的函数
#     func_choice = {"insert": insert, "delete": delete, "update": update, "select": select}
#     sql_list = sql.replace(",", " ").split()  # 将sql解析成列表形式
#     if sql_list[0] == "select":                   #如果用户输入的sql语句是查询
#         sql_dict = {"from": [], "where": [], "limit": []}
#         tag = False
#         for item in sql_list:                        #根据sql解析出sql_dict
#             if tag and item in sql_dict:
#                 tag = False
#             if not tag and item in sql_dict:
#                 tag = True
#                 key = item
#                 continue
#             if tag:
#                 sql_dict[key].append(item.strip('\"'))
#         func_choice.get(sql_list[0])(sql_dict)                  #解析出sql_dict后，传入查询函数，并调用查询函数
#     elif sql_list[0] == "insert":                        #如果用户输入的sql语句是创建
#         sql_dict = {}
#         sql_list.remove("insert")
#         sql_dict.setdefault("values",sql_list)                 #解析出sql_dict，传入创建函数
#         insert(sql_dict)                                           #调用创建函数
#     elif sql_list[0] == "delete":                               #解析出sql_dict后，传入删除函数，并调用查询函数
#         delete_id = int(sql_list[1])                                #获取用户要删除的id
#         delete(delete_id)                                       #调用删除函数
#     elif sql_list[0] == "update":                                 #如果用户输入的sql语句是修改
#         sql_dict = {"set":[],"where":[],"update":[]}
#         tag = False
#         for items in sql_list:                                #根据用户的sql，解析出sql_dict字典
#             if tag and items in sql_dict:
#                 tag = False
#             if not tag and items in sql_dict:
#                 tag = True
#                 key = items
#                 continue
#             if tag:
#                 sql_dict[key].append(items.strip('\"'))
#         update(sql_dict)                                 #传入修改函数，并调用修改函数
#     return sql_list
#
# def insert(sql_dict):                                     #创建信息函数
#     with open("staff_table","ab+") as f:
#         offs = -100
#         while True:
#             f.seek(offs,2)
#             lines = f.readlines()
#             if len(lines) > 1:
#                 last = lines[-1]
#                 break
#             offs *= 2
#         last = last.decode(encoding="utf-8")
#         last_id = int(last.split(",")[0])
#         new_id = last_id + 1
#         record = sql_dict.get("values")
#         record.insert(0,str(new_id))
#         record_str = ",".join(record)+"\n"
#         f.write(bytes(record_str,encoding="utf-8"))
#         f.flush()
#         print("\033[1;31m创建成功 \033[0m")
#
# def delete(delete_id):                               #删除函数
#     with open("staff_table","r",encoding="utf-8") as f1,open("staff_table_bak","w",encoding='utf-8') as f2:
#         del_count = 1
#         for line in f1:
#             if del_count != delete_id:
#                 f2.write(line)
#             elif del_count == delete_id:
#                 pass
#             del_count += 1
#     print("\033[1;31m删除成功 \033[0m")
#     os.remove("staff_table")                      #删除原员工信息文件
#     os.rename("staff_table_bak","staff_table")              #修改新员工信息文件名
#
# def update(sql_dict):                             #修改函数
#     set_list = sql_dict.get("set")                   #获取要修改的内容
#     set_key = set_list[0]
#     where_list = sql_dict.get("where")               #获取要修改的文件内容
#     with open("staff_table", "r", encoding="utf-8") as f1, open("staff_table_bak", "w", encoding='utf-8') as f2:
#         for line in f1:
#             title = "id,name,age,phone,dept,enroll_date"
#             dic = dict(zip(title.split(","),line.split(",")))          #将文件每一行打包成字典的形式
#             if logic_action(dic,where_list):                           # 逻辑判断，调用逻辑判断函数
#                 line = line.replace(dic[set_key],set_list[2])           #修改需要修改的那一行内容
#             f2.write(line)                                              #将原文件写进新文件
#     print("\033[1;31m修改成功 \033[0m")
#     os.remove("staff_table")
#     os.rename("staff_table_bak", "staff_table")
#
# def select(sql_dict):                                         #查询函数
#     title = "id,name,age,phone,dept,enroll_date"
#     f = open("staff_table", "r", encoding="utf-8")    # 1、找到数据库
#     res = []
#     for line in f:
#         dict1 = dict(zip(title.split(","), line.strip().split(",")))
#         where_list = sql_dict.get("where")
#         if len(where_list) != 0:
#             if logic_action(dict1, where_list):  # 逻辑判断，调用逻辑判断函数
#                 res.append(line.strip())
#         else:
#             res = f.readlines()
#     print("查询到的信息有 \033[1;35m %s \033[0m 条"%len(res))
#     for i in res:
#         print("分别是\033[1;35m [%s]\033[0m "%i)
#     return res
#
# def logic_action(dict1, where_list):       #逻辑判断函数，如果文件的信息符合要求，就返回True
#     tag = False
#     if where_list[1] == "<":
#         if dict1[where_list[0]] < where_list[2]:
#             tag = True
#     elif where_list[1] == "=":
#         if dict1[where_list[0]] == where_list[2]:
#             tag = True
#         else:pass
#     elif where_list[1] == ">":
#         if dict1[where_list[0]] > where_list[2]:
#             tag = True
#         else:pass
#     elif where_list[1] == "like":
#             if where_list[2] in dict1[where_list[0]]:
#                 tag = True
#     return tag
#
# while True:
#     try:
#         info_display()
#     except IndexError as e:
#         print("【%s】，请输入正确的格式"%e)              #如果用户输入的格式不正确，就打印提示
d = {'2': ['Elijah Yang', '26', '13650000000', 'IT', '2015-07-15'], '1': ['Alex Li', '22', '13651054608', 'IT', '2013-04-01']}
# l = list(d.keys())
# print(len(l))
# ------------------------------
# for k,v in d.items():
#     print(k,v)
# ------------------------------
# del d['2']
# print(d)
# s = input('>>>').strip()
# print(s.split('\''))

#
# l = ['1','2','3','4',]
# print(d['1'].index('IT'))
# for k,v in d.items():
#     print(k)
#     print(v)

# s= 'select name , age from staff_table where age > 22'
# res = s[s.index(' ',s.index('where')):].split()
# res = res.split()
# res = s[s.index(' '):s.index('from')].replace(' ','').split(',')
# print(res)

# import time
#
# s = '2015-03-18'
# a = time.strptime(s, "%Y-%m-%d")
# print(a)


# s = '36'
# if s.isdigit():
#     print('T')
# else:
#     print('F')

