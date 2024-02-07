
# conversions
print("Conversions".center(60, "-"))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("The number {num} {num} {num}".format(num=36))
print("The number {num} {num:f} {num:b}".format(num=36))
print("The number {num:10} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=3645656678))
print("The number {num:10} {num:f} {num:b}".format(num=36))

print("Alignment".center(60, "-"))
print("{num:15} Tendulkar".format(num=3))
print("{num:15} Tendulkar".format(num="Sachin"))
print("{num:>15} Tendulkar".format(num="Sachin"))       # right justified
print("{num:^15} Tendulkar".format(num="Sachin"))       # center justified
print("{num:<15} Tendulkar".format(num="Sachin"))       # left justified

print("-" * 60)
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

from math import pi, e
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("-" * 60)
print("one googol is {}".format(10 ** 100))
print("one googol is {:,}".format(10 ** 100))       # thousands seperator

print("{pi:10.3}".format(pi=pi))
print("{pi:010.3}".format(pi=pi))
print("{pi:010.4}".format(pi=pi))
print("{pi:010.5}".format(pi=pi))

print("-" * 60)
print("{:60}".format("Python Programming"))
print("{:*<60}".format("Python Programming"))
print("{:*^60}".format("Python Programming"))
print("{:*>60}".format("Python Programming"))
print("Python Programming".center(60, "*"))

print("-" * 60)
print("{0:10.2f}\n{1:10.2f}".format(pi, e))

print("{0:.2} \t {1:.2}".format(pi, e))
print("{0} \t {1}".format(pi, e))

print("{:b}".format(10))            # binary
print("{:#b}".format(10))           # binary

print("-" * 60)



