
def greet():
    print("Greetings Mr. Sachin, Welcome to the event")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.....")

# gname and non default argument and cty as a default argument
def greetGstCty(gname, x =100, cty="Mumbai"):
    print(f"Greetings Mr.{gname} from {cty}, Welcome to the event......")


greet()

print("-" * 60)

greetGst("Rahul")

print("-" * 60)
greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", cty = "Bangalore")

print("-" * 60)

def admsn(fname, lname, dob, gender, qlf, loc, perc):
    print(f"First Name is  :{fname}")
    print(f"Last Name is   :{lname}")
    print(f"Date of Birth  :{dob}")
    print(f"Gender         :{gender}")
    print(f"Qualification  :{qlf}")
    print(f"Location       :{loc}")
    print(f"Percentage     :{perc}")

admsn(qlf= "M tech", dob = "15/04/1995", lname="Slater", fname="Micheal", loc="Delhi", perc="87%", gender="M")

print("-" * 60)

def sum(x, y):
    return x + y

a  = 10
b = 20
print(f"The sum of {a}  amd {b} are :{sum(a, b)}")

print("-" * 60)
def arithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return (sum, diff, prod, quot)

res = arithmeticCalc(20, 8)
print(res)

# recursive call to find the factorial of a number
# recursive call to generate fibanocci series

print("-" * 60)
# variable length arguments

def prodAll(*numbers):       # *numbers can accept more than one value
    print(numbers)
    print(*numbers)         # unpacking
    num = 1
    for number in numbers:
        num *= number

    return num

res = prodAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)

def AcceptPlyrDet(**details):
    print(details)
    for k, v in details.items():
        print(k, "=>", v)

AcceptPlyrDet(name="Sachin", age=32, runs=75, oppn="SA")

print("-" * 60)

def fun1():
    "This is a doc string"
    # This is a comment
    print("Hello World \n")

fun1()
print(fun1.__doc__)
print("-" * 60)

def fun1(x, y):
    """
    function - fun1(x, y)
    ---------------------
    1. if x and y are integers then the result is the sum of the numbers
    2. if x and y are strings then the result is the concate the  strings
    3. if x and y are of different data type then throws an error
    """

    return x + y

print("-" * 60)
help(fun1)