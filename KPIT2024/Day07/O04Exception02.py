


x = 10
y = "0"

try:
    res = x / y
    flag = False
except Exception as e:
    print("exception".center(60, "-"))
    print("Exception raised....")
    print(e)
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