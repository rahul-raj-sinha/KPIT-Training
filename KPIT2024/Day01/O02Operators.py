
"""
Arithematic
Conparison or relational
Logical
Bitwise
Ternary

"""

print("Arithematic Operator".center(60, "="))
a = 10
b = 3

print(f"a = {a} and b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")     # floor division

print("Augmentor".center(60, "-"))
# =, +=, -=, *=, /=
x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

print("Comparison".center(40, "-"))
# ==, !=, >, < , >=, <=

print(f"1 == 1 :{1 == 1}")

print(f"1 == 2 :{1 == 2}")

print("Logical Operators".center(60, "-"))
# and, or, not

print(1 == 1 and 1 == 1)
print(1 == 1 and 1 == 2)

print(1 == 1 or 1 == 2)
print(1 == 2 or 1 == 2)

print(not(1 == 1 or 1 == 2))
print(not(1 == 2 or 1 == 2))

print("-" * 60)
print(f"ord(a) :{ord('a')}")        # iterger representation of unicode character
print(f"ord(A) :{ord('A')}")        # iterger representation of unicode character
print(f"ord(a) :{ord('z')}")        # iterger representation of unicode character
print(f"ord(Z) :{ord('Z')}")        # iterger representation of unicode character

print("apple" > "oramge")
print("apple" < "orange")

print("Bitwise Operators".center(40, "-"))
print(5 | 3)
print(5 & 3)
print(5 ^ 3)
print(5 << 1)
print(8 << 1)

# ternary operator
age = 15
print("Eligible" if age >= 18 else "Not Eligible")


