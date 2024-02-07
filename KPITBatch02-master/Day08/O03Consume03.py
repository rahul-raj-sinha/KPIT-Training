
import sys

sys.path.append("C:/Delhi")

for pth in sys.path:
    print(pth)

import gurgaon.mymodule as m

m.greet("Swetha")

ply1 = m.Player("Badri", 20)
ply1.get_details()