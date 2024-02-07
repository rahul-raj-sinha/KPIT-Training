
import gurgaon.mymodule as m
import sys

for pth in sys.path:
    print(pth)

print("-" * 60)

m.greet("Waheed")

ply1 = m.Player("Krishna Sai", 20)
ply1.get_details()