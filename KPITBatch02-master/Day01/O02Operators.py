
print("Arithmetic Operators".center(60, "-"))
print(f"10 + 3 = {10 + 3}")
print(f"10 - 3 = {10 - 3}")
print(f"10 * 3 = {10 * 3}")
print(f"10 / 3 = {10 / 3}")
print(f"10 // 3 = {10 // 3}")       # floor division

print("-" * 60)
print(10 % 3)
print(10 ** 3)

print("Augmentor".center(60, "-"))
#  =, +=, -=, *=
x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

print("Comparison Operator".center(60, "-"))
# ==, >, >=, <, <=
a = 10
b = 15

print(f"a == b :{a == b}")
print(f"a > b :{a > b}")
print(f"a < b :{a < b}")

print("Logical Operator".center(60, "-"))
# and, or, not
print(f"1==1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1==1 and 2 == 2 :{1 == 1 and 2 == 1}")

print(f"1==1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"1==1 or 2 == 2 :{1 == 1 or 2 == 1}")

print(f"not(1 == 1 or 2 == 2) :{not(1 == 1 or 2 == 2)}")
print(f"not(1 == 2 or 2 == 2) :{not(1 == 2 or 2 == 1)}")

print("-" * 60)
print(f"ord('a') :{ord('a')}")      # integer representation of unicode character
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print("bitwise operators".center(60, "-"))

print(f"5 | 3 :{ 5 | 3}")
print(f"5 & 3 :{ 5 & 3}")
print(f"5 ^ 3 :{ 5 ^ 3}")
print(f"5 << 1:{ 5 << 1}")
print(f"8 << 1:{ 8 << 1}")
print(f"5 << 2:{ 5 << 2}")
print(f"5 >> 1:{5 >> 1}")
print(f"16 >> 1 :{16 >> 1}")

print("ternary".center(60, "-"))
a = 10
print("Eligible" if a > 18 else "Not eligible")








