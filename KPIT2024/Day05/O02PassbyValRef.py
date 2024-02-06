
def passByval(x):
    print(x)
    x += 100
    print(f"The value of x is :{x}")

def passByref(lst):
    print(f"Inside :{lst}")
    lst.append("Ruben")
    print(f"Inside :{lst}")

y = 50
print(f"Before y :{y}")
passByval(y)
print(f"After y :{y}")

print("-" * 60)
custNames = ["Jack", "Mike", "Kennedy"]
print(f"Before custNames :{custNames}")
passByref(custNames)
print(f"After custNames :{custNames}")

