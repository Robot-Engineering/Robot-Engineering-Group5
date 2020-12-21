# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 19:30:11 2020

@author: Admin
"""

from traits.api import HasTraits, Enum
from traitsui.api import View
import matplotlib.image 
import matplotlib.pyplot
 
class Ui(HasTraits):
    list_choice = ["张三", "李四", "王五"]
    choice_=Enum(list_choice)
    choice_choose=choice_
    if choice_choose == '张三':
        img = matplotlib.image.imread(r'C:\Users\Admin\Desktop\101.jpg')
        matplotlib.pyplot.imshow(img)
        matplotlib.pyplot.show()
    if choice_choose == '李四':
        img = matplotlib.image.imread(r'C:\Users\Admin\Desktop\102.jpg')
        matplotlib.pyplot.imshow(img)
        matplotlib.pyplot.show()
    if choice_choose == '王五':
        img = matplotlib.image.imread(r'C:\Users\Admin\Desktop\102.jpg')
        matplotlib.pyplot.imshow(img)
        matplotlib.pyplot.show()
            
    view=View("choice_", title=u"学生图片信息",width=800,height=600,resizable=True)
    
ui=Ui()
ui.configure_traits()