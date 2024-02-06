# """
# import path from .pth file present in python native directory
# C:\Users\Kiran\AppData\Local\Programs\Python\Python311
# """

# import sys
#
# print([pth for pth in sys.path])

import gurgaon.mymodule as m
from gurgaon.mymodule import Player

m.greet("Rohith")

ply1 = Player("Yuvraj Singh", 45)
ply1.get_details()