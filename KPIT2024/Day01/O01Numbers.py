
"""
int
float
complex
"""

a = 10
b = -10

print(a)
print(type(a))      # RTTI - runtime type identification
print(b)
print(type(b))

print("-" * 60)

c = 10.9
d = -10.9

print(c)
print(type(c))
print(d)
print(type(d))

print("-" * 60)

e = +2e3
f = -2e3

print(e)
print(type(e))
print(f)
print(type(f))

print("-" * 60)
g = 10+2j
h = 10- 2j

print(g)
print(type(g))
print(h)
print(type(h))

print("-" * 60)
x = 2 + 3.5
print(type(x))

x = 1
y = 2.5
z = x + y
print("x =", type(x))
print("y =", type(y))
print("z =", type(z))

print("conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(11)       # decimal
print(0b11)     #binary
print(0b101)    # Binary
print(0o11)     # octal
print(0o101)    # octal
print(0xe)      #hexa
print(0xa)      #hexa

print("Number 'System Conversion".center(60, "-"))
a = 100
print(bin(a))
print(oct(a))
print(hex(a))

