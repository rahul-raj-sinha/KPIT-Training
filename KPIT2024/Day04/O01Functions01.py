
def greet():
    print("Greetings Mr.Sachin, Welcome to the event")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event....")

# gname is non default argument and cty is a default arg
def greetGstCty(gname,  cty="Mumbai"):
    print(f"Greetings Mr.{gname} from {cty}, Welcome to the event.....")

greet()
print("-" * 60)

greetGst("Rahul")
greetGst("Sourav")

print("-" * 60)
greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)

def admsn(fname, lname, dob, qlf, gender, loc, idprf):
    print(f"First Name    :{fname}")
    print(f"Last Name     :{lname}")
    print(f"Date of Birth :{dob}")
    print(f"Qualification :{qlf}")
    print(f"Gender        :{gender}")
    print(f"Location      :{loc}")
    print(f"ID Proof      :{idprf}")

admsn(loc="chennai", idprf="Pan Card", dob="15/01/1998", gender="Male", fname='John', lname = "Nixon", qlf="MBA")

print("-" * 60)
# variable length arguments - fun(*args, **kwargs)

# *numbers  - can accept more than one value and store it in a tuple
def prodAll(*numbers):
    print(numbers)
    prod = 1
    for number in numbers:
        prod *= number
    return prod

res = prodAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)

def extractDetails(**details):
    print(f"details :{details}")
    print("-" * 60)
    for k, v in details.items():
        print(k + " => " + str(v))


extractDetails(name="Sachin", age=36, runs=185, oppn="Aus", venue="MCG")

print("-" * 60)

def multiplyMe(a, b):
    return a * b

x = 5
y = 8
print(f"The product of {x} and {y} is :{multiplyMe(x, y)}")

print("-" * 60)
# recursive calls
# 1. factorial of a number
# 2. fibanocii series

# doc strings  - help on the functions

def fun():
    # this is a comment
    "this is a doc string"

    print("Hello World")


fun()
print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    fun1(x, y)
    ----------

    1. if x and y are numbers then we get a sum of the numbers as output
    2. if x and y are strings then it will get concatinated
    3. if x and y are of different datatypes then it will throw and error

    """
    return x + y

print("-" * 60)

print(fun1(10, 20))

print("-" * 60)

help(fun1)

print("-" * 60)

def arithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x/ y
    return sum, diff, prod, quot

res = arithCalc(20, 8)
print(f"res :{res}")
