# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 23:12:19 2020

@author: Administrator
"""

from traits.api import HasTraits, Int
from traitsui.api import View, Item, Group
class EasyMenu(HasTraits):
    rawx = Int
    rawy = Int
    width = Int
    height = Int
    length = Int
    radian = Int
    
view1=View(
     Group(
        Item(name = 'rawx', label=u'x坐标'),
        Item(name = 'rawy', label=u'y坐标'),
        Item(name = 'width', label=u'宽度'),
        Item(name = 'height', label=u'长度'),
        label=u'InsertRectangle',
        show_border=True
    ),
    
    Group(
        Item(name = 'rawx', label=u'x坐标'),
        Item(name = 'rawy', label=u'y坐标'),
        Item(name = 'radian', label=u'半径'),
        label=u'InsertCircle',
        show_border=True
    ),
    
    Group(
        Item(name = 'rawx', label=u'x坐标'),
        Item(name = 'rawy', label=u'y坐标'),
        Item(name = 'length', label=u'长度'),
        label=u'InsertLine',
        show_border=True
    ),
)

sam = EasyMenu()
sam.configure_traits(view=view1)
    