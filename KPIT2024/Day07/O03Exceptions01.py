

x = 10
y = None

try:
    res = x / y
    flag = False
except ZeroDivisionError as z:
    print("exception".center(60, "-"))
    print("Exception raised....")
    print(z)
    flag = False
except TypeError as t:
    print("exception".center(60, "-"))
    print("Exception raised....")
    print(t)
    flag = False
else:
    print("else".center(60, "-"))
    print(f"The result is {res}")
    flag = True
finally:
    print("finally".center(60, "-"))
    if flag:
        print("the porcess of division completed....")
    else:
        print("division of numbers not successful")