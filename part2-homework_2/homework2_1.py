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
# Important py file：json
# How To：Execute directly
# 个人发挥：
# 个人博客地址：http://blog.csdn.net/dragonyangang

import json

menu ={
    '北京':{
        '西城区':{
            '西单':{
                '大悦城':{},
                '明珠':{},
                '君太':{},
            },
            '中南海':{}
        },
        '朝阳区':{
            '三里屯':{
                '优衣库':{},
                '太古里':{},
                '工体':{},
            },
            '国贸':{
                '银泰中心':{},
                '万达广场':{},
                '北京电视台':{},
            },
        },
        '海淀区':{
            '五道口':{
                'soho':{},
                'google':{},
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平区':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '天津':{
        '河东区':{},
        '河西区':{},
        '南开区':{
            '南开大学':{},
            '天津大学':{},
        },
    },
}

#将menu序列化存储至文件中

with open("menu_serialize.json",mode="w") as f :
    f.write(json.dumps(menu))
print("Finished！You've already serialized a dict to a json-file !")
