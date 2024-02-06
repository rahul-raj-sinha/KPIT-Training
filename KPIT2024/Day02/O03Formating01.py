
# emulate C style from printf

format = "Welcome %s, what a %s player"
print(f"format :{format}")
values = ("Sachin", "superb")       # tuple
print(values)

print(format % values)
print("Welcome %s, what a %s player" % ("Sachin",  "superb"))
print("-" * 60)

format = "Welcome %s with a rating of %.3f, what a %s player"
print(format % ("Sachin", 4, "class"))
print(format % ("Sachin", 4.8, "class"))
print(format % ("Sachin", 4.82, "class"))
print(format % ("Sachin", 4.825370, "class"))
print(format % ("Sachin", 4.8253787, "class"))

# unix Shell Syntax
print("-" * 60)
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
res =  tmpl.substitute(name = "Rahul", adj="class")
print(res)

# Python string syntax
print("-" * 60)
print("Welcomw {}, what a {} player for {}".format("Sachin", "class", "India"))
print("Welcomw {0}, what a {1} player for {2}".format("Sachin", "class", "India"))
print("Welcomw {2}, what a {0} player for {1}".format( "class", "India", "Sachin"))
print("Welcomw {pname}, what a {adj} player for {ctry}".format( adj="class", ctry="India", pname="Sachin"))
print("Welcome {name}, your rating {rating}".format(name="Sachin", rating=4))
print("Welcome {name}, your rating {rating:.3f}".format(name="Sachin", rating=4.8766666))

print("-" * 60)
from math import pi, e
print(f"PI={pi} and Euler's constant = {e}")
print("PI={} and Euler's constant = {} and magic number = {}".format(pi, e, 40585))
print("PI={p:.2f} and Euler's constant = {e:.2f} and magic number = {m}".format(p=pi, e=e, m=40585))

print("-" * 60)
full_name = ["Sachin", "Tendulkar"]
print(full_name)
print("Mr.{name}".format(name = full_name))
print("Mr.{name}".format(name = full_name[0]))
print("Mr.{fname} {lname}".format(fname=full_name[0], lname=full_name[1]))

print("-" * 60)
import math
print(__name__)
print(math.__name__)

print("the {mod.__name__} module gives the value of pi = {mod.pi} and eulers = {mod.e}".format(mod=math))
