"""
int
float
complex
"""

a = 10
b = -10

print(f"a :{a}")
print(type(a))              # RTTI - Runtime type identification
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 10.0
d = -10.0
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = +2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 60)
g = 3j
h = -3j

print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 60)
print(max(2, 4, 5, 1, 3))
print(min(2, 4, 5, 1, 3))

print("-" * 60)
x = 3 + 2.5
print(type(x))

x = 1
y = 3.5
z = x + y

print("x=", type(x))
print("y=", type(y))
print("z=", type(z))

print("Conversion".center(60, "-"))
a = 10
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60,  "-"))
print(11)       # decimal
print(0b11)     # Binary
print(0b101)    # binary
print(0o11)     # octal
print(0o101)    # octal
print(0xe)      # hexa
print(0xa)      # hexa


print("Conversion".center(60, "-"))
a = 100
print(oct(a))
print(hex(a))
print(bin(a))