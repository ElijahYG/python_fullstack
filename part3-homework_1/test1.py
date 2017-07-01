#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Elijah"
__date__ = "2017/6/18 22:59"

# s = 'backend www.baidu.com'
# print(s.split()[1])

# def show_list(file):   # 查询显示并将文本生成程序需要的字典和列表
#      backend_list = []
#      backend_all_dict = {}
#      backend_dict = {}
#      server_list = []
#      with open(file,'r') as f:    # 读取haproxy文件
#          for line in f:
#
#              line = line.strip()
#              if line.startswith('backend') == True:    # 判断是否是backend开头，读取backend信息写到backend_list中
#                  backend_name = line.split()[1]
#                  backend_list.append(backend_name)    # 将文件中backend加到列表中
#                  server_list = []   # 清空server_list里的记录，遇到新backend可以输入新的server_list
#              elif line.startswith('server') == True:    # 判断是否是server开头，读取server信息写到backend_all_dict中
#                  backend_dict['name'] = line.split()[1]    # 读取文件中server的name
#                  backend_dict['IP'] = line.split()[2]    # 读取文件中server的IP
#                  backend_dict['weight'] = line.split()[4]    # 读取文件中server的weight
#                  backend_dict['maxconn'] = line.split()[6]   # 读取文件中server的maxconn
#                  server_list.append(backend_dict.copy())    # 将backend中的信息加到server_list中,此处需要用copy
#                  backend_all_dict[backend_name] = server_list    # 将server信息对应backend存到字典中
#      return (backend_list,backend_all_dict)    # 返回backend和server信息
#
# show_list('haproxy.conf')

# l = []
# d = {'www.baidu.com':['1.1.1.1','1.1.1.1',20,3000],'www.python.org':['2.2.2.2','2.2.2.2',10,2000],}
# s = ""
# for i in d.keys():
#     print(i)
#     for j in d :
#         print(d[i][0])
#         # print(d[i][1])
#         # print(d[i][2])
#         # print(d[i][3])

#-----------------------------------------------------------------------------------------------------------
# #最后将内存写入文件用
# l = []
# d = {'www.baidu.com':['1.1.1.1','1.1.1.1',20,3000],'www.python.org':['2.2.2.2','2.2.2.2',10,2000],}
# s = ""
# for i in d.keys():
#     print(i)
#     print(d[i][0])
#     print(d[i][1])
#     print(d[i][2])
#     print(d[i][3])
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
# #backend信息修改
# l = []
# d = {'www.baidu.com':['1.1.1.1','1.1.1.1',20,3000],'www.python.org':['2.2.2.2','2.2.2.2',10,2000],}
# s = ""
# d['www.baidu.com'][0] = '3.3.3.3'
# print(d['www.baidu.com'][0])
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
# #backend信息删除
# l = []
# d = {'www.baidu.com':['1.1.1.1','1.1.1.1',20,3000],'www.python.org':['2.2.2.2','2.2.2.2',10,2000],}
# s = ""
# del d['www.baidu.com']
# print(d)
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
# info = '''
# global
#         log 127.0.0.1 local2
#         daemon
#         maxconn 256
#         log 127.0.0.1 local2 info
# defaults
#         log global
#         mode http
#         timeout connect 5000ms
#         timeout client 50000ms
#         timeout server 50000ms
#         option  dontlognull
#
# listen stats :8888
#         stats enable
#         stats uri       /admin
#         stats auth      admin:1234
#
# frontend oldboy.org
#         bind 0.0.0.0:80
#         option httplog
#         option httpclose
#         option  forwardfor
#         log global
#         acl www hdr_reg(host) -i www.oldboy.org
#         use_backend www.oldboy.org if www
#
# backend www.oldboy.org
#         server 100.1.1.1 100.1.1.1 weight 20 maxconn 3000
#
# backend www.baidu.com
#         server 100.1.1.2 100.1.1.2 weight 20 maxconn 2000
#
# backend www.google.com
#         server 192.168.1.1 192.168.1.1 weight 10 maxconn 1000
# '''
# print(info[:info.index('\nbackend ')])
#-----------------------------------------------------------------------------------------------------------
# import os
# info=os.getcwd()
# listfile=os.listdir(info)
# print(listfile)


