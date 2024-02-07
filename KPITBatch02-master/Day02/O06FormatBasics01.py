
# emulate c style printf

format = "Hello %s what a %s player"
print(format)
values = ("Sachin", "superb")
print(values)
print(format % values)
print("Hello %s what a %s player" % ("Sachin", "superb"))
format = "Welcome %s, your rating of %.3f, what a %s player"
print(format % ("Sachin", 4, "class"))
print(format % ("Sachin", 4.7, "class"))
print(format % ("Sachin", 4.787775, "class"))
print("Welcome %s, your rating of %.3f, what a %s player" % ("Sachin", 4.789923, "class"))

print("-" * 60)
# unix style
from string import Template
tmpl = Template("Hello $name what a $adj player")
# print(f"tmpl :{tmpl}")
print(tmpl.substitute(name = "Sachin", adj="class"))

print("-" * 60)

# format strings from python

print("Welcome {}, what a {} player for {}".format("Sachin", "super", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "super", "India"))
print("Welcome {1}, what a {2} player for {0}".format("Sachin", "super", "India"))
print("Welcome {pname}, what a {adj} player for {ctry}".format(ctry =
"India", pname="Sachin", adj="super"))

print("Welcome {pname} your rating of {rating}, what a player".format(pname="Sachin", rating=4))

print("Welcome {pname} your rating of {rating:.3f}, what a player".format(pname="Sachin", rating=4.7888823))

print("-" * 60)
#interpolation
from math import pi, e
print(f"PI={pi} and e={e}")

print("PI={} and Eulers constant = {}".format(pi, e))
print("PI={0} and Eulers Constant = {1}".format(pi, e))

print("-" * 60)
full_name = ["Sachin", "Tendulkar"]
print(f"fullname :{full_name}")

print("Mr.{pname}".format(pname=full_name))
print("Mr.{name[0]} {name[1]}".format(name=full_name))

print("-" * 60)
import math
print(__name__)
print(math.__name__)

print("The {mod.__name__} module gives the values of pi = {mod.pi} and eulers constant e = {mod.e}".format(mod=math))

