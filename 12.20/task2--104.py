import os
import os.path
import xlrd
import xlwt
from xlutils.copy import copy

def geturlPath():
    path = r'testdat\104'
    dirs = os.listdir(path)
    for dir in dirs:
        pa = path + "\ " + dir
        if not os.path.isdir(pa):
            yield pa
    if "jpg" in pa:
        print(True)
        #打开students.xlsx文件
        work_book=xlrd.open_workbook('testdat\students.xlsx')

        #将xlrd的workbook变成xlwtworkbook对象
        work_book_new = copy(work_book)

        #写入信息
        new_sheet = work_book_new.get_sheet(0)
        new_sheet.write(4,2,pa)
        work_book_new.save(r'testdat\students.xlsx')
    else:
        print(False)
        work_book=xlrd.open_workbook('testdat\students.xlsx')
        
        work_book_new = copy(work_book)
        
        new_sheet = work_book_new.get_sheet(0)
        color = xlwt.easyxf('pattern: pattern solid, fore_colour yellow;')
        new_sheet.write(4,1,"104",color)
        work_book_new.save(r'testdat\students.xlsx')
            
if __name__ == '__main__':
    for item in geturlPath():
        print(item)