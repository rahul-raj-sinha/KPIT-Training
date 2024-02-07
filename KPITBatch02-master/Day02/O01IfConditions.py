
a = int(input("Enter the first number :"))
print(f"a :{a}")
print(type(a))

if (a < 10): print(f"a is a single digit number :{a}")

runs = 80
if (runs > 100):
    print("its a good score to defend....")
print("God match to watch....")

b = int(input("Enter the second  number :"))
print(f"b :{b}")
print(type(b))

c = int(input("Enter the third number :"))
print(f"c :{c}")
print(type(c))

if (a >= b and a >= c):
    print(f"a is the greatest :{a}")
elif (b >= a and b >= c):
    print(f"b is the greatest :{b}")
else:
    print(f"c is the greatest :{c}")
