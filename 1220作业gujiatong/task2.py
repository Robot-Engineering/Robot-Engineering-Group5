# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 21:25:17 2020

@author: Admin
"""
import xlrd
import xlwt
from xlutils.copy import copy

path=r'C:\Users\Admin\Desktop\testdat\testdat\studentdata.xlsx'
sd=xlrd.open_workbook(path)
sheet1=sd.sheets()[0]
sheet=copy(sd)
sheet2=sheet.get_sheet(0)
row_sum=sheet1.nrows
row={}
color = xlwt.easyxf('pattern: pattern solid, fore_colour yellow;')

for i in range(1,row_sum):
    row[i]=sheet1.row_values(i)
    if row[i][2]=='':
        print(row[i])  #输出没有照片的学生信息
        sheet2.write(i, 1, sheet1.cell(i, 1).value, color)  #没有照片的添加高亮
        
sheet.save(r'C:\Users\Admin\Desktop\testdat\testdat\studentdata1.xlsx')

