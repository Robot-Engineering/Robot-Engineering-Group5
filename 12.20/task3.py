import matplotlib.image as im
import matplotlib.pyplot as plt
import os
from traits.api import HasTraits, Str
from traitsui.api import View, Item, Group

#需要读取的路径
class Information(HasTraits):
    
    view1 = View(
        Group(
            path_name1 = r'testdat\101'

            for item in os.listdir(path=path_name1):
                img = im.imread(os.path.join(path_name1,item))
                plt.imshow(img)
                plt.show()
            
            label=101.jpg
        )
    )

  
    path_name2 = r'testdat\102'

    for item in os.listdir(path=path_name2):
        img = im.imread(os.path.join(path_name2,item))
        plt.imshow(img)
        plt.show()

    path_name3 = r'testdat\103'

    for item in os.listdir(path=path_name3):
        img = im.imread(os.path.join(path_name3,item))
        plt.imshow(img)
        plt.show()
