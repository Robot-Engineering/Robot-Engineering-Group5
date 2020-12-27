# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 18:47:08 2020

@author: Admin
"""

import pymysql

user_name1='\''+input("请输入用户姓名：")+'\''    #输入信息
goodsinfo1='\''+input("请输入商品名称：")+'\''
date1='\''+input('请输入送达时间：（YY年MM月DD日 XX:XX）')+'\''
price1=float(input('请输入价格：'))
address1='\''+input('请输入送货地址：')+'\''

#连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', password=input("password:"), db='test')

cursor = conn.cursor()

sql = '''create table if not exists robot_order(
    id int auto_increment primary key,
    user_name varchar(32),
    goodsinfo varchar(32),
    date varchar(32),
    price float,
    address varchar(64)
    )engine=INNODB default charset=utf8;'''
cursor.execute(sql)

#插入数据
sql_1="INSERT INTO robot_order(user_name,goodsinfo,date,price,address) values(user_name1,goodsinfo1,date1,price1,address1)"
cursor.execute(sql_1)

sql_2="SELECT * FROM robot_order"
cursor.execute(sql_2)
result = cursor.fetchall()  # 获取全部查询结果，并赋值给result
print(result)

cursor.close()
conn.close()