# python_fullstack
## [我的博客](http://blog.csdn.net/dragonyangang "我的博客")

# 第二模块：作业1-6：用户登陆
  
    Author: Elijah
    Time: 2017-05-31
    Function: 模拟登陆
      1. 用户输入帐号密码进行登陆
      2. 用户信息保存在文件内
      3. 用户密码输入错误三次后锁定用户
    Need Environment：Python 3.5 、PyCharm
    Feature：
      1、开始提供用户选择功能界面：登陆 or 注册
      2、用户在输入用户名或者密码时可以中断退出
      3、用户名和密码是对应的，所以判断用户和密码是否正确时要对应判断
      4、用户注册时要判断用户名是否已经被注册，已经被注册的不能再次注册
      5、单独有一个文件存储被锁定的用户名，以提供用户检查
    Important py file：getpass
    How To：Execute directly

- 个人博客地址: http://blog.csdn.net/dragonyangang/article/details/72835866

# 第二模块：作业2：三级目录

    Author: Elijah
    Time: 2017-05-31
    Function: 三级菜单：
      1. 运行程序输出第一级菜单
      2. 选择一级菜单某项，输出二级菜单，同理输出三级菜单
      3. 返回上一级菜单和顶部菜单
      4. 菜单数据保存在文件中
    Need Environment：Python 3.5 、PyCharm
    Feature：
    Important py file：getpass
    How To：Execute directly
    
- 个人博客地址: http://blog.csdn.net/dragonyangang/article/details/72851011

# 第二模块：作业3：购物车

    Author: Elijah
    Time: 2017-06-07
    Function:购物车
      1. 商品信息- 数量、单价、名称
      2. 用户信息- 帐号、密码、余额
      3. 用户可充值
      4. 购物历史信息
      5. 允许用户多次购买，每次可购买多件
      6. 余额不足时进行提醒
      7. 用户退出时 ，输出当次购物信息
      8. 用户下次登陆时可查看购物历史
      9. 商品列表分级显示
    Need Environment：Python 3.5 、PyCharm
    Feature：
      1、实现了基本登陆功能，包括验证用户是否存在、是否被锁定
      2、用户成功登陆后可进入购物车功能
      3、购物车实现了商品分级显示
      4、每次用户登陆时显示历史购物信息
      5、用户余额不足时可以进行充值
      6、用户可以多次购买多件商品
      7、用户退出时显示本次购物商品信息
    Important py file：getpass,time
    How To：Execute directly
    
- 个人博客地址: http://blog.csdn.net/dragonyangang/article/details/72862830

# 第三模块：作业1：HAproxy配置文件操作
    Readme
    Author: Elijah
    Time: 2017-06-18
    Function:HAproxy配置文件操作
        1. 根据用户输入输出对应的backend下的server信息
         2. 可添加backend 和sever信息
        3. 可修改backend 和sever信息
        4. 可删除backend 和sever信息
        5. 操作配置文件前进行备份
        6. 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作
    Need Environment：Python 3.5 、PyCharm
    Move：
    Feature：
    Important py file：os
    How To：Execute directly
    个人发挥：用模块化的编程思想
- 个人博客地址：http://blog.csdn.net/dragonyangang/article/details/74067566

# 第三模块：作业2：员工信息表程序
    Readme
    Author: Elijah
    Time: 2017-06-20
    Function:员工信息表程序
        可进行模糊查询，语法至少支持下面3种:
            select name,age from staff_table where age > 22
            select  * from staff_table where dept = "IT"
            select  * from staff_table where enroll_date like "2013"
        查到的信息，打印后，最后面还要显示查到的条数
        可创建新员工纪录，以phone做唯一键，staff_id需自增
        可删除指定员工信息纪录，输入员工id，即可删除
        可修改员工信息，语法如下:
         UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
        1. 支持至少三种方法的select查询，并在最后显示查询到的条数。
        2. 创建新员工记录，以phone为唯一键，staff_id自增
        3. 输入员工id可删除指定员工信息记录
        4. 可以使用UPDATE命令修改指定员工信息。
    Need Environment：Python 3.5 、PyCharm
    Move：
    Feature：
    Important py file：re、time
    How To：Execute directly
    个人发挥：用模块化的编程思想
- 个人博客地址：http://blog.csdn.net/dragonyangang/article/details/74069329

# 第三模块：作业3：ATM

    Readme
    Author: Elijah
    Time: 2017-06-24
    Function:ATM
        1. 指定最大透支额度
        2. 可取款
        3. 定期还款（每月指定日期还款，如15号）
        4. 可存款
        5. 定期出账单
        6. 支持多用户登陆，用户间转帐
        7. 支持多用户
        8. 管理员可添加账户、指定用户额度、冻结用户等
    Need Environment：Python 3.5 、PyCharm
    Move：
    Feature：
    Important py file：re、datetime
    How To：Execute directly
    个人发挥：用模块化的编程思想
- 个人博客地址：http://blog.csdn.net/dragonyangang/article/details/74071248

[回到顶部](#readme)
