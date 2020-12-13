# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 23:47:06 2020

@author: Administrator
"""

from traits.api import HasTraits, Int
from traitsui.api import View, Item, Group

class EasyMenu(HasTraits):
    pass
    
    
    
    
view1=View(
    Group(
        label=u'Open',
        show_border=True
    ),
    
    Group(
        label=u'Save',
        show_border=True
    ),
    
    Group(
        label=u'Exit',
        show_border=True
    ),
)

sam = EasyMenu()
sam.configure_traits(view=view1)