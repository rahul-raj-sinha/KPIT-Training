
import sys
import os

# print(os.cpu_count())
# commandline arguments
print(sys.argv)

sys.path.append("c:\Delhi")

print([pth for pth in sys.path])


import gurgaon.mymodule as m
from gurgaon.mymodule import Player

m.greet("Srikanth")

ply1 = Player("Vengsarkar", 64)
ply1.get_details()