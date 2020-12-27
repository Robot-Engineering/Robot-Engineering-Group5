# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 22:24:24 2020

@author: Admin
"""

import pymysql

robot_type1='\''+input("请输入物流机器人型号：")+'\''    #输入信息
date1='\''+input("请输入物流机器人生产日期：（YY年MM月DD日）")+'\''
cond1='\''+input('请输入机器人的状态：')+'\''
orderid1=int(input('请输入待物流机器人配送的订单编号：'))

#连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', password=input("password:"), db='test')

cursor = conn.cursor()

sql = '''create table if not exists robot_info(
    id int auto_increment primary key,
    robot_type varchar(32),
    date varchar(32),
    cond varchar(32),
    orderid int
    )engine=INNODB default charset=utf8;'''
cursor.execute(sql)

#插入数据
sql_1="INSERT INTO robot_info(robot_type,date,cond,orderid) values(robot_type1,date1,cond1,orderid1)"


sql_2 = "SELECT * FROM robot_info"
cursor.execute(sql_2)
result = cursor.fetchall()  # 获取全部查询结果，并赋值给result
print(result)

cursor.close()
conn.close()