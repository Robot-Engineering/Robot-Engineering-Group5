# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:16:55 2020

@author: Admin
"""

import pymysql

user_name1='\''+input("请输入用户姓名：")+'\''    #输入信息
orderid1=int(input('请输入用户订单编号：'))+'\''
address1='\''+input('请输入用户地址信息：')+'\''

#连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', password=input("password:"), db='test')

cursor = conn.cursor()

sql = '''create table if not exists address_info(
    id int auto_increment primary key,
    user_name varchar(32),
    orderid int,
    address varchar(64)
    )engine=INNODB default charset=utf8;'''
cursor.execute(sql)

#插入数据
sql_1="INSERT INTO address_info(user_name,orderid,address) values(user_name1,orderid1,address1)"


sql_2 = "SELECT * FROM address_info"
cursor.execute(sql_2)
result = cursor.fetchall()  # 获取全部查询结果，并赋值给result
print(result)

sql_3 = "UPDATE address_info set orderid=123 WHERE user_name='Tom'"
cursor.execute(sql_3)

sql_4 = "DELETE FROM address_info"
cursor.execute(sql_4)



cursor.close()
conn.close()