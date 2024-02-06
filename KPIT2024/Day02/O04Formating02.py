
# conversions
print("Conversions".center(60, "-"))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("-" * 60)
print("{num} {num} {num}".format(num=36))
print("{num} {num:f} {num:b}".format(num=36))
print("{num:10} {num:f} {num:b}".format(num=36))
print("{num:5} {num:f} {num:b}".format(num=36))
print("{num:5} {num:f} {num:b}".format(num=3681250981))

print("Alignmant".center(50, "-"))
print("{num:10}Sachin".format(num=3))
print("{num:10}Sachin".format(num="Ramesh"))

print("-" * 60)
print("{num:<15} Tendulkar".format(num = "Sachin"))
print("{num:^15} Tendulkar".format(num = "Sachin"))
print("{num:>15} Tendulkar".format(num = "Sachin"))

print("-" * 60)
print("{num:*^30}".format(num="Sachin"))
print("{num:05}".format(num=25))

print("-" * 60)
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

from math import pi, e
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))
