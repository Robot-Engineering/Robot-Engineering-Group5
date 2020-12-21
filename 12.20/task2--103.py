import os
import os.path
import xlrd
import xlwt
from xlutils.copy import copy

def geturlPath():
    path = r'testdat\103'
    dirs = os.listdir(path)
    for dir in dirs:
        pa = path + "\ " + dir
        if not os.path.isdir(pa):
            yield pa
    if "jpg" in pa:
        print(True)
    else:
        print(False)
        
    #打开students.xlsx文件
    work_book=xlrd.open_workbook('testdat\students.xlsx')

    #将xlrd的workbook变成xlwtworkbook对象
    work_book_new = copy(work_book)

    #写入信息
    new_sheet = work_book_new.get_sheet(0)
    new_sheet.write(3,2,pa)
    work_book_new.save(r'testdat\students.xlsx')
            
if __name__ == '__main__':
    for item in geturlPath():
        print(item)