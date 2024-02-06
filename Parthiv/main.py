# 1
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(i, end="")
#     print()

# 2
# n = 1
# for i in range(4):
#     for j in range(i+1):
#         print(n, end=" ")
#         n += 1
#     print()

# 3


# l1 = list()
# print(f"li: {l1}")
# print(type(l1))


# nums = [0, 1, 2, 2, 3, 0, 4, 2]
# val = 2
# n = len(nums)
# for i in range(n):
#     if nums[i] == val:
#         nums.remove(nums[i])
#     print(nums[i])

# print(len(nums))
# print(nums)
# print(nums[7])

# for i in range(len(l1)):
#     print(l1[i], end="")
# print()

# nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
# val = 2
# n = len(nums)
# nums.sort()
# for i in range(n-1):
#     if (nums[i] == val):
#         nums.remove(nums[i])

# print(len(nums))
# print(nums)


# l1 = [1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2,
#       3, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# while 1 in l1:
#     l1.remove(1)
# print(l1)

# while 2 in l1:
#     l1.pop(l1.index(2))
# print(l1)


############### sort###################

# from copy import deepcopy
# l1 = [1, 2, 3, [1, 2, 3], 5]
# l2 = l1.copy()
# print(l2)
# l2.extend([7, 8, 9])
# print(l2)
# l1[3].extend([4, 5])
# print(l2)

# l3 = [2, 4, 6, [1, 2, 3], 8, 10]
# l4 = deepcopy(l3)
# print(l4)
# l3[3].extend([4, 5])
# print(l4)
# print(l3)


# a = [1, 3, 2, 4, 5]

# for i in range(1, len(a)):
#     for j in range(1, len(a)-i-1):
#         if (a[j] > a[j+1]):
#             a[j], a[j+1] = a[j+1], a[j]

# print(a)


# l1 = [10, 'zebra', 4, 'apple', 9, 'yellow', 'blue', 1, 'violet', 'green', 6, 'pink', 'red',
#       8, 'orange', 'cat', 2, 'dog', 'maroon', 5, 'white', 7, 3, 192, 1234, 29, 270, 2345]

# temp = sorted([i for i in l1 if type(i) == int])
# temp2 = sorted([i for i in l1 if type(i) == str])

# print(temp + temp2)

# cities = ['vishakapatnam', 'mumbai',  'ooty', 'pune',
#           'chennai', 'delhi', 'kolkata']
# cities.reverse()
# print(cities)
# res = sorted(cities, key=len)
# print(res)

# d1 = dict([('name', "Parthiv"), ('age', 34), ('runs', 45)])
# # print(d1)
# # print(type(d1))

# for key, val in d1.items():
#     print("key: {}\tvalue: {}".format(key, val))

# nums = [2, 7, 4]
# k = 181
# temp = []
# while (k > 0):
#     d = k % 10
#     temp.append(d)
#     k = k // 10
# temp.reverse()
# print(temp)
# n = len(nums) - len(temp)
# z = [0 for i in range(n)]
# res = z + temp
# print(res)
# ans = []
# for i in range(len(nums)):
#     ans.append(nums[i] + res[i])
# print(ans)


# nums = [1, 2, 1, 3, 2, 5]
# d = dict()
# for i in nums:
#     d[i] = 0
# for i in nums:
#     if i in nums:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
# ans = []
# for key, val in d.items():
#     if (val == 1):
#         ans.append(key)

# print(ans)


# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)


# n = 5
# print(fact(n))


# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)


# n = int(input())
# for i in range(1, n+1):
#     print(fib(i), end=" ")

# def insertionSortRecursive(arr, n):
#     if n <= 1:
#         return
#     insertionSortRecursive(arr, n - 1)
#     last = arr[n - 1]
#     j = n - 2
#     while (j >= 0 and arr[j] > last):
#         arr[j + 1] = arr[j]
#         j = j - 1
#     arr[j + 1] = last


# arr = [1, 3, 2, 5, 4]
# insertionSortRecursive(arr, 5)
# print(arr)

# from collections import namedtuple


# def art(a, b):
#     nmd = namedtuple("Arithmetic", ["sum", "diff", "prod", "quot"])
#     sm = a + b
#     df = a - b
#     pd = a * b
#     qt = a / b

#     res = nmd(sum=sm, diff=df, prod=pd, quot=qt)
#     return res


# res = art(5, 3)

# print(res.sum)
# print(res.diff)
# print(res.prod)
# print(res.quot)

# print('-'*60)


# def art(a, b):
#     sm = a + b
#     df = a - b
#     pd = a * b
#     qt = a / b
#     return (sm, df, pd, qt)


# sm, df, pd, qt = art(5, 3)

# print(sm, df, pd, qt)


# def prodAll(*num):
#     print(num)
#     print(*num)


# print(prodAll(5, 4, 3))


# def accept(**details):
#     print(details)
#     for k, v in details.items():
#         print(k, "=>", v)


# accept(name="Sachin", age=32, run=75)

# from functools import reduce
# from calendar import month_abbr
# exp = [8500, 10000, 32000, 15000, 2500, 6000, 50000]
# ans = list(map(lambda x: x/85, exp))

# print(ans)
# print(list(month_abbr))

# months = ['apr', 'aug', 'dec', 'feb', 'mar', 'may',
#           'nov', 'oct', 'jan', 'jun', 'jul', 'sep']

# res = sorted(months, key=list(
#     (map(lambda month: month.lower(), list(month_abbr)))).index)
# print(res)

# l = [1, 3, 2, 5, 4]
# res = reduce(lambda x, y: x if x > y else y, l)
# res1 = reduce(lambda x, y: x+y, l)
# print(res)
# print(res1)

# players = {
#     'sachin': [350, 250, 300, 400, 385],
#     'rahul': [200, 300, 450, 150, 185],
#     'sehwag': [300, 350, 425, 400, 360],
#     'sourav': [150, 300, 350, 200, 400],
#     'laxman': [250, 200, 300, 450, 185],
# }

# avg_score = {name: (lambda scr: sum(scr) / len(scr))(score)
#              for name, score in players.items()}
# # print(avg_score)
# l1 = [x for x in players.values()]

# l2 = [l1[i][j] for i in range(len(l1))
#       for j in range(len(l1[0])) if l1[i][j] >= 200]

# l3 = {name: [scr for scr in score if scr > 200]
#       for name, score in players.items()}

# print(l3)

# class Sample:
#     rais = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay

#     def fullname(self):
#         return f"Fullname is: {self.first} {self.last} "

#     def apply(self):
#         self.pay = int(self.pay * self.rais)


# emp1 = Sample("Parthiv", "Sen", 50000)

# print(Sample.fullname(emp1))
# print(emp1.fullname())
# emp1.apply()
# print(emp1.pay)
# print(emp1.__dict__)

# from datetime import datetime


# class Employee:
#     def __init__(self, name, dob):
#         self.name = name
#         self.dob = dob
#         self.age = self.calcAge()

#     @classmethod
#     def DOB(cls, name, dob):
#         return cls(name=name, dob=dob)

#     def calcAge(self):
#         curr = datetime.now().year
#         dob = self.dob[-4:]
#         age = curr - int(dob)
#         return age

#     def __str__(self):
#         return f"Name is {self.name}\nAge is {self.age}"


# name = "Parthiv"
# dob = "12-12-2002"

# emp = Employee.DOB(name, dob)
# print(emp)

######################################################
# Function Decorators with arguments
# def test(a, b):
#     def dec(fnc):
#         def inner(x, y):
#             print(a, b)
#             print(x, y)
#         return inner
#     return dec

# @test(10, 12)
# def fun(a, b):
#     print(a, b)

# fun(10, 20)

######################################################
# Class Decorators with argument

# class Dec(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def outdec(self, fnc):
#         def dec(self, a, b):
#             print(self.x, self.y)
#             fnc(a, b)
#             return a, b


# @Dec(34, 42)
# def fun(a, b):
#     print(20, 10)


# fun(10, 20)

#####################################################
'''
Import a python file as module
1. .py file get converted into .pyc file and stored in a folder __pycache__
2. python will check for .pth file in your native directory(where python.exe is present)
3. Checks for the library path that is present in sys.path
4. checks for the date and time of creation of .py vs .pyc files. Expects .pyc file to have the latest date or time of modification.
'''

'''
.       Any Single character
^       Search at the beginning of string
$       Search at the end of string
*       Zero or more occurance
?       Zero or one occurance
+       One or more occurance
{n}     Exactly n times
{n,}    Atleast n times
{n,m}   Min n times and max m times
[ ]     Character class
( )     Grouping
|       Alternation (OR operator)
\       Escape - supress the meaning of regex
\w      Matches Alpha Numeric characters
\W      Matches Special characters
\d      Matches Digits
\D      Matches Non digits
\s      Matches Space
\S      Matches Non-space
\b      Word boundary
\B      Non-word boundary
\A      Beginning of string
\Z      End of string
match()
search()
findall()
finditer()
compile()
'''
