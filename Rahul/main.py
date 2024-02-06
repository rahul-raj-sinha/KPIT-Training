# Factorial using recursive
# def Fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * Fact(n - 1)
#
#
# num = int(input())
#
# print(Fact(num))


# Fibonacci Series Using Recursive
# def fib(n):
#     if n == 1 or n==0:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# n = int(input())
# for i in range(n):
#     print(fib(i),end=" ")


# variable length arguements
# def prodAll(*numbers):
#     print(numbers)
#     print(*numbers)
#     num=1
#     for number in numbers:
#         num*=number
#
#     return num
#
# print(prodAll(1,2,3,4,5))


# variable length arguments in form dictionaries

# def AcceptPlyDet(**details):
#     print(details)
#     for k, v in details.items():
#         print(k,"-", v)
# AcceptPlyDet(name='Ram',age=32,runs=55,oppn="SA")


# def fun1(x,y):
#     """
#     hi bye gn
#     """
#
#
#     return x+y


# Conversion of currency from rupees to dollars
# Expenses= [8500,10000,32000,15000,2500,6000,50000]


# Assignment
# Sort the month based on calender
# from calendar import month_abbr
# a=list(month_abbr)
# print(a)
# months=['apr','aug','dec','feb','mar','may','nov','oct','jan','jun','jul','sep']
# b=sorted(months,key=list(map(lambda month: month.lower(), list(month_abbr))).index)
# print(b)


# dict1 = {
#     'sachin': [350, 250, 300, 400, 385],
#     'rahul': [200, 300, 450, 150, 185],
#     'sehwag': [300, 350, 425, 400, 360],
#     'laxman': [345, 300, 200, 150, 190],
#     'yuvraj': [190, 150, 120, 250, 275]
# }
# scores = {k: sum(v) for k, v in dict1.items()}
# print(scores)

# scores=[scores for scores in dict1.values()]
# print(scores)

# l=[]
# for i in range(len(scores)):
#     for j in range(len(scores)):
#         l.append(scores[i][j])
# print(l)

# a=[scores for scores in dict1.values() for scores in scores]
# print(a)


# avg_score = {name: (lambda x: sum(x) / len(x))(score) for name, score in dict1.items()}
# print(avg_score)
# def avg(list):
#     a = sum(list) / len(list)
#     return a
# avg_score = {name: avg(score) for name, score in dict1.items()}
# print(avg_score)

# scores={k:[scores for scores in scores if scores >=200] for k, scores in dict1.items()}
# print(scores)


# class Person:
#     def __int__(self, name, age):
#         self.name=name
#         self.age=age
# p1 = Person()
# print(p1.name)
# print(p1.age)


# def outerFun():
#
#
#     def innerFun():
#         print("Hello")
#
#     return innerFun
# Inref=outerFun()
# Inref()


# def outer(greet):
#     def inner(sep):
#         def innermost(gname):
#             print(greet,sep,gname)
#         return innermost
#     return inner
#
#
# engGrt=outer("Welcome")
# hndGrt=outer("Namaste")
#
# engGrtSngArrow=engGrt("------->")
# engGrtdblArrow=engGrt("======>")
# hndGrtSngArrow=hndGrt("------->")
# hndGrtdblArrow=hndGrt("======>")
#
# engGrtSngArrow("Rahul")
# engGrtdblArrow("Raj")
# hndGrtSngArrow("Aditya")
# hndGrtdblArrow("Vijay")

# Decorator
# def bankjob(fnc):
#     def helper(amount):
#         print("Logging In")
#         fnc(amount)
#         print("logging Out")
#         print("-"*60)
#     return helper
#
# @bankjob #it will take deposit as an argument
# def deposit(amt):
#     print(f"Amount {amt} credited into the account...")
#
#
# @bankjob
# def withdraw(amt):
#     print(f"Amount {amt} dedited from the account...")
#
# deposit(45000)
# withdraw(30000)

# bankjob(deposit)
# bankjob(withdraw)

# import time
#
# def bankjob(fnc):
#     def helper(amount):
#         start_time=time.time()
#         print("Logging In")
#         fnc(amount)
#         end_time=time.time()
#         print("logging Out")
#         et=end_time-start_time
#         print(et)
#         print("-"*60)
#     return helper
#
#
# @bankjob #it will take deposit as an argument
# def deposit(amt):
#     print(f"Amount {amt} credited into the account...")


#
# @bankjob
# def withdraw(amt):
#     print(f"Amount {amt} dedited from the account...")

# deposit(45000)
# withdraw(30000)


# def dec1(fnc):
#     def inner():
#         print("-"*20)
#         fnc()
#         print("#"*20)
#     return inner
# def dec2(fnc):
#     def inner():
#         print("*"*20)
#         fnc()
#         print("_"*20)
#     return inner
#
# @dec1
# @dec2
# def fun():
#     print("Welcome")
#
# fun()


# OOPS

# class Player:
#     def get_runs(self):
#         print("runs scored....")
#
#
#
# sachin=Player()
# sachin.get_runs()
#
# print(type(sachin))
# print(isinstance(sachin, Player))
# print(isinstance(sachin, object))
# print(isinstance(sachin, str))


# class Player:
#     def __init__(self):         # Constructor
#         print("Player Initialized....")
#
#     def get_runs(self):
#         print("runs scored....")
#
# ply1=Player()
# ply1.get_runs()
# ply1.__init__()
#
# print("-"*90)
#
# ply2=Player()
# ply2.get_runs()
# ply2.__init__()


# class Player:
#     def __init__(self):         # Constructor
#         print("Player Initialized....")
#         self.name="Ram"          #Instance Variable
#         self.age=22
#
#     def get_details(self):
#         print(f"Name is {self.name}\nAge is {self.age}")
#
# ply1=Player()
# ply1.get_details()
#
# print("-"*60)
# ply2=Player()
# ply2.name="Rajesh"     # we can change variable value by object and it's possible only in python
# ply2.age=22
# ply2=Player()
# ply2.get_details()


# class Player:
#     def __init__(self, name, age):         # Constructor
#         print("Player Initialized....")
#         self.name=name        #Instance Variable
#         self.age=age
#
#     def get_details(self):
#         print(f"Name is {self.name}\nAge is {self.age}")
# ply1=Player(name="Ram", age=22)
# ply1.get_details()
#
# print("-"*60)
#
# ply2=Player(name="Rajesh", age=21)
# ply2.get_details()
#
#
# print("-"*60)
#
#
#
#
# ply2.runs=150
# print(ply2.get_details())
# print(ply2.runs)
#
# print("-"*60)
#
# print(ply1.get_details())
# # print(ply1.runs)


# class Player:
#     def __init__(self, name, age):         # Constructor
#         print("Player Initialized....")
#         self.name=name        #Instance Variable
#         self.age=age
#
# ply1=Player(name="Rajesh", age=21)
# ply2=Player(name="Rajesh", age=21)\
#
# my_dict1=vars(ply1)
# my_dict2=ply1.__dict__
# my_dict3=ply2.__dict__
#
#
# print(my_dict1)
# print(my_dict2)
#
# print(my_dict3)


#
# class Player:
#     team = "India"
#
#     def __init__(self, name, age):         # Constructor
#
#         print("Player Initialized....")
#         self.name=name        #Instance Variable
#         self.age=age
#
#     def get_details(self):
#         print(f"Name is {self.name}\nAge is {self.age}")
#
#
# ply1=Player(name="Ram", age=23)
# ply1.get_details()
#
# ply2=Player(name="Ram", age=23)
# ply2.get_details()
#
# print("-"*60)
#
# print(f"Player :{Player.team}")
# print(f"Ply1 :{ply1.team}")
# # print(f"Ply2 :{Ply2.team}")
#
# print("-"*60)
#
#
# ply1.team="MI"
# print(f"Player :{Player.team}")
# print(f"Ply1 :{ply1.team}")
# print(ply2.__dict__)
# # print(f"ply2 :{ply2.team}")
#
# print("-"*60)
#
# ply2.team="RCB"
# print(ply2.team)
# print(ply2.__dict__)


# ******* CLASS METHOD (V.imp)
# class Player:
#     team = "India"
#
#     def __init__(self, name, age):         # Constructor
#
#         print("Player Initialized....")
#         self.name=name        #Instance Variable
#         self.age=age
#
#     def get_details(self):
#         print(f"Name is {self.name}\nAge is {self.age}")
#
#     @classmethod
#     def CreatePlayer(cls, fname, lname, age):
#         print(f"factory.....")
#         return cls(f"{fname} {lname}", age)       #Calls Constructor
#
#
#
#
# ply1=Player(name="ram",age=23)
# ply1.get_details()
#
# print("-"*60)
#
#
# ply2=Player.CreatePlayer("Virat","Kohli", 24)
# ply2.get_details()
#


# class Player:
#
#     def __init__(self, name, age):  # Constructor
#
#         print("Player Initialized....")
#         self.name = name  # Instance Variable
#         self.age = age
#
#     def __str__(self):
#         print(f"Name is {self.name}\nAge is {self.age}")
#
#
# ply1 = Player(name="ram", age=22)
# # print(str(ply1))
#
# # print(ply1)   #both are same(line 472 and 474)
#
#
# print(ply1)


#
# class Employee:
#     def __init__(self,name, salary):
#         self.name=name
#         self.salary=salary
#
#
#     def __str__(self):
#         return f"Name is {self.name}\nSalary is {self.salary}"
#
#
#     def __eq__(self, other):
#         return self.salary==other.salary
#
#     def __gt__(self, other):
#         return self.salary>other.salary
#
# emp1=Employee(name="Kevin", salary=65000)
# print(emp1)
# print("-"*60)
# emp2=Employee(name="Kavya", salary=60000)
# print(emp2)
# print("-"*60)
# if emp1==emp2:
#     print("{}'s is salary {} is equal to {}' 2 salary {}".format ( emp1.name, emp1.salary,emp2.name,emp2.salary))
#
# else:
#     print("{}'s is salary {} is not equal to {}' 2 salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
#
#
#
#
# if emp1<emp2:
#     print("{}'s is salary {} is not greater than {}' 2 salary {}".format ( emp1.name, emp1.salary,emp2.name,emp2.salary))
#
# else:
#     print("{}'s is salary {} is greater than {}' 2 salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
#
#
# print("-"*60)





#
# from functools import total_ordering
#
# @total_ordering
# class Employee:
#     def __init__(self,name, salary):
#         self.name=name
#         self.salary=salary
#
#
#     def __str__(self):
#         return f"Name is {self.name}\nSalary is {self.salary}"
#
#
#     def __eq__(self, other):
#         return self.salary==other.salary
#
#     def __gt__(self, other):
#         return self.salary>other.salary
#
# emp1=Employee(name="Kevin", salary=65000)
# print(emp1)
# print("-"*60)
# emp2=Employee(name="Kavya", salary=60000)
# print(emp2)
# print("-"*60)
# if emp1==emp2:
#     print("{}'s is salary {} is equal to {}' 2 salary {}".format ( emp1.name, emp1.salary,emp2.name,emp2.salary))
#
# else:
#     print("{}'s is salary {} is not equal to {}' 2 salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
#
#
#
#
# if emp1<emp2:
#     print("{}'s is salary {} is not greater than {}' 2 salary {}".format ( emp1.name, emp1.salary,emp2.name,emp2.salary))
#
# else:
#     print("{}'s is salary {} is greater than {}' 2 salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
#
#
# print("-"*60)
#
#
# print(emp1>=emp2)


# class Employee:
#     def __init__(self,name, salary):
#         self.name=name
#         self.salary=salary
#         self.tech=['C','C++','Java','Python','Javascript']
#
#
#     def __str__(self):
#         return f"Name is {self.name}\nSalary is {self.salary}"
#
#     def __iter__(self):
#         return iter(self.tech)
#
#     def append(self,val):
#         self.tech.append(val)
#
#     def __len__(self):
#         return len(self.tech)
#
#
#     def __getitem__(self, idx): #getter method
#         return self.tech[idx]
#
#
#     def __setitem__(self, idx, val):
#         self.tech[idx]=val   # we will not use return as we are modifying the value not returning it
#
#
#
#
# emp1=Employee(name="Kevin", salary=65000)
# print(emp1)
#
# print("-"*60)
#
# print([tech for tech in emp1])
#
#
# print("-"*60)
#
# emp1.append("Fluter")
# print([tech for tech in emp1])
#
# print("-"*60)
#
# print(len(emp1))
#
# print("-"*60)
#
# tech1=emp1[2] #getter method
# print(tech1)
#
# print("-"*60)
# emp1[5]="ReactJS"  #setter method
# print([tech for tech in emp1])
#
# print("-"*60)





# class Product:
#     def __init__(self, price):
#         # self.name=name
#         self.__price=price    #private Variable
#
#
#     def getprice(self):
#         return self.__price
#
#
#     def setprice(self, prc):
#         if prc<0:
#             raise ValueError("Price can not be less than Zero")    #we are using for exceptions
#
#         else:
#             self.__price=prc
#
#
#     def deleteprice(self):
#         self.__price=0
#
# import sys # for exceptional cases
#
# try:
#     pepsi=Product(50)
#     print(pepsi.getprice())
#     pepsi.setprice(-50)
#     print(pepsi.getprice())
#     pepsi.deleteprice()
#     print(pepsi.getprice())
# except:
#     print("Exception")
#     print(sys.exc_info()[0])
#     print(sys.exc_info()[1])




# class Product:
#     def __init__(self, price):
#         # self.name=name
#         self.__price=price    #private Variable
#
#
#     def getprice(self):
#         return self.__price
#
#
#     def setprice(self, prc):
#         self.__price=0
#
#
#     def deleteprice(self):
#         self.__price=0
#
#
#
#
#     price=property(getprice,setprice,deleteprice)
#
#
# coke=Product(60)
# print(coke.price)
# coke.price=120
# print(coke.price)
# del coke.price
# print(coke.price)










# class Animal:
#     def __init__(self):
#         print("Animal...")
#         self.age=1
#
#     def eat(self):
#         print("Animal Eat")
#
#
# class Birds(Animal) :
#     def fly(self):
#         print("Birds can fly")
#
#
# class Fish(Animal):
#     def swim(self):
#         print("Fish can Swim")
#
#
# crow=Birds()
# crow.eat()
# crow.fly()
#
# print(crow.__dict__)
#
# shark=Fish()
# shark.eat()
# shark.swim()
#
# print(shark.__dict__)




# class Animal:
#     def __init__(self):
#         print("Animal...")
#         self.age=1
#
#     def eat(self):
#         print("Animal Eat")
#
#
# class Birds(Animal) :
#     def fly(self):
#         print("Birds can fly")
#
#
# class Fish(Animal):
#     def swim(self):
#         print("Fish can Swim")






# def add_country_codes(func):
#     def wrapper(numbers):
#         country_codes = ["+91" + number for number in numbers]
#         return func(sorted(country_codes))
#     return wrapper
# @add_country_codes
# def formatted_numbers(numbers):
#     for number in numbers:
#         formatted = f"{number[:3]} {number[3:8]} {number[8:]} "
#         print(formatted)
# #sample input
# num_count = 3
# phone_numbers = [
#     "07895462130",
#     "919875641230",
#     "9195969878"]
# print(formatted_numbers(phone_numbers))





# from datetime import datetime
# class Employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         # self.age=self.createEmp(name,date)
#
#     def __str__(self):
#         return f"Name is {self.name}\nAge is {self.age}"
#
#     @classmethod
#     def createEmp(cls,name,age):
#         today_date=datetime.today()
#         year=datetime.strptime(age,"%d/%m/%Y")
#         # today=datetime.now()
#
#         age=today_date.year-year.year-((today_date.month,today_date.day)<(year.month, year.day))
#
#         return cls(name,age)
#
# # Employee.createEmp(name="kennedy", date= "23/04/1990")
# emp1=Employee.createEmp("Kennedy","24/04/1990")
#
# print(emp1)
#
#









# FIle Handling

# fl=open("C:\\Users\\RAHULR24\\Downloads\\file1.txt","r")  # if "r" is not there than it will take "r" by default

# st=fl.read(100) #will read entire content
# st=fl.readline()     #can read one line
# st=fl.readlines()  #can read all lines and stored in list form
# print(st)
# for st in fl.readlines():
#     print(st)

# print(st)
# fl.close()


# fw=open("C:\\Users\\RAHULR24\\Downloads\\myfile.txt","w")  # if "r" is not there than it will take "r" by default
# # st=input("Enter content for the file:")
#
# # fw.write(st)
# l1="this is 1st line \n"
# l2="this is 2nd line \n"
# l3="this is 3rd line \n"
# fw.writelines([l1,l2,l3])
# fw.close()


# fa=open("C:\\Users\\RAHULR24\\Downloads\\myfile.txt","a")
# st=input("Enter content for the file:")
# fa.write(st+'\n')
# fa.close()



# Write a code to accept lines from the user until the user says 'NO'.
# fw = open("C:\\Users\\RAHULR24\\Downloads\\myfile.txt","w")  # if "r" is not there than it will take "r" by default
#
#
# while True:
#     st = input("Enter content for the file:")
#     if st=="No" or st=="no":
#         break
#     else:
#         fw.write(st)
#
# fw.close()



# # Random Position
#
# fl=open("file1.txt","rb")
#
# pos=fl.seek(50,0)
# print(f"pos: {pos}")
#
# pos=fl.seek(100,1)
# print(f"pos: {pos}")
#
# pos=fl.seek(-45,1)
# print(f"pos: {pos}")


# import csv
#
# data = [
#     ['501', 'Jack', '28', 'HR', '65000'],
#     ['235', 'Jill', '34', 'FIN', '35000'],
#     ['150', 'John', '26', 'AC', '25000'],
#     ['325', 'Jai', '21', 'DEV', '55000'],
#     ['450', 'Guru', '38', 'DEV', '85000'],
#     ['182', 'Sita', '32', 'PRC', '75000'],
#     ['297', 'Gita', '36', 'SUP', '60000'],
# ]
#
# colnames = ['empid', 'empname', 'age', 'dept', 'salary']
# with open("empres.csv", "w") as CSVW:
#     writer = csv.writer(CSVW)
#     writer.writerow(colnames)
#
#     for row in data:
#         writer.writerow(row)



# import json
# JFR=open("books.json","r")
# jsonFile=json.load(JFR)
# for  book in jsonFile['books']:
#     print(book['name'])
#     print("-" * len(book['name']))
#     for k,v in book.items():
#         print(k, "=>", v)
#     print("-"*60)


# import json
# player = {
#     'players':[
#         {'id': 'P101', 'Name': 'Sachin Tendulkar', 'Matches': 585, 'runs': 28500, 'age': 38},
#         {'id': 'P102', 'Name': 'Sourav Ganguly', 'Matches': 430, 'runs': 19400, 'age': 36},
#         {'id': 'P103', 'Name': 'Rahul Dravid', 'Matches': 390, 'runs': 18500, 'age': 35},
#         {'id': 'P104', 'Name': 'Virendra Sehwag', 'Matches': 410, 'runs': 23500, 'age': 34},
#         {'id': 'P105', 'Name': 'VVS Laxman', 'Matches': 298, 'runs': 15500, 'age': 36},
#         {'id': 'P106', 'Name': 'Virar Kholi', 'Matches': 450, 'runs': 23000, 'age': 38},
#         {'id': 'P107', 'Name': 'Yuvraj Singh', 'Matches': 520, 'runs': 19400, 'age': 36},
#         {'id': 'P108', 'Name': 'MS Dhoni', 'Matches': 460, 'runs': 18500, 'age': 35},
#         {'id': 'P109', 'Name': 'Md Kaif', 'Matches': 345, 'runs': 12400, 'age': 34},
#         {'id': 'P110', 'Name': 'Suresh Raina', 'Matches': 410, 'runs': 15500, 'age': 36},
#     ]
# }

# JFW=open("IndianTeam.json","w")
# json.dump(player,JFW)
# JFW.close()











# Lambda
# fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
#
# # Print the Fibonacci series up to 2 elements
# print("Fibonacci series upto 2:")
# print(fib_series(2))
#
# # Print the Fibonacci series up to 5 elements
# print("\nFibonacci series upto 5:")
# print(fib_series(5))















# Classmethod
# BANKooPs
# class Bank:
#     def __init__(self,name,age,Aadhar,accountNum,money):
#         print("Account Created")
#         self.name=name
#         self.age=age
#         self.Aadhar=Aadhar
#         self.money=money
#         self.accountNum=accountNum
#     @classmethod
#     def createAcc(cls):#IN CLASS METHOD WE CAN TAKE INPUT AND ASSIGN VALUES TO THE INSTANCE VARIABLES TOO
#         import random
#         name=input("Enter the name")
#         money=int(input("Enter the money to be deposited when account is created"))
#         age=int(input("Enter Age"))
#         Aadhar=input("Enter the Aadhar Number").upper()
#         accountNum=random.randint(10**9,(10**10)-1)
#         return cls(f"{name}",age,f"{Aadhar}",accountNum,money)
#     def AfterCreation(self):
#         print( "Account Successfully Created\n")
#         print(f"Details are\n Name-{self.name}\n Age-{self.age}\n Aadhar details are -{self.Aadhar}\n AccountNumber is -{self.accountNum}\n account balance - {self.money}")
#
#     def Deposit(self):
#         if self.money==0:
#             print("Zero account Balance")
#             n=int(input("Enter the money to be deposited"))
#             self.money+=n
#         else:
#             n = int(input("Enter the money to be deposited"))
#             self.money+=n
#         print(f"Total Money-{self.money}")
#         return self.money
#     # def __str__(self):
#     #     return f"The details are Name-{self.name}\n Age-{self.age}\n Initial Amount-{self.money}\n AccountNo-{self.accountNum}\n Aadhar Details-{self.Aadhar}"
#     def Transaction(self,amount):
#         if self.money>=amount:
#             self.money-=amount
#             print(f"Transaction Successful,Updated account balance is Rs{self.money}")
#         else:
#             print("Insufficient Balance")
#
# Person1=Bank.createAcc()
#
# Person1.AfterCreation()
# Person1.Deposit()
# n=int(input("Amount to be transacted"))
# Person1.Transaction(n)
#




# Lambda Calender
# lst = list(range(1, 11))
# print(f"lst :{lst}")
#
# squares = list(map(lambda x: x ** 2, lst))
#
# print(f"squares :{squares}")
#
#
# # conversion of currency from rupees to dollars
# expenses = [8500, 10000, 32000, 15000, 2500, 6000, 50000]
#
# # assignment
# # sort the m     onths based on calendar
# months = ['apr', 'aug', 'dec', 'feb', 'mar', 'may', 'nov', 'oct', 'jan', 'jun', 'jul', 'sep']
#
# print("-" * 60)
# from calendar import month_abbr
# print(list(month_abbr))
# res = sorted(months, key=list(map(lambda month: month.lower(),list(month_abbr))).index)
# print(f"res :{res}")









# Daughters Mangoes:

# t_mango = int(input("Enter the value:\n"))
# d1 = t_mango//3                 # d1, d2, d3 = daughter 1,2,3
# extra = t_mango%3
#
# d2 = d1+extra
# extra2 = d2 % 3
# d3 = d2 // 3
# final = d1+d2+d3
# res = t_mango-final           # rem = remaining mangoes
# print(d1)
# print(d2)
# print(d3)
# print(final)








# Morse Code
# MORSE_CODE_DICT = {
#     'A': '.-', 'B': '-...',
#     'C': '-.-.', 'D': '-..', 'E': '.',
#     'F': '..-.', 'G': '--.', 'H': '....',
#     'I': '..', 'J': '.---', 'K': '-.-',
#     'L': '.-..', 'M': '--', 'N': '-.',
#     'O': '---', 'P': '.--.', 'Q': '--.-',
#     'R': '.-.', 'S': '...', 'T': '-',
#     'U': '..-', 'V': '...-', 'W': '.--',
#     'X': '-..-', 'Y': '-.--', 'Z': '--..',
#     '0': '-----', '1': '.----', '2': '..---',
#     '3': '...--', '4': '....-', '5': '.....',
#     '6': '-....', '7': '--...', '8': '---..',
#     '9': '----.',
#     ',': '--..--', ':': '---...', "'": '.----.',
#     '!': '-.-.--', '.': '.-.-.-', '?': '..--..'
# }
#
# def text_to_morse(text):
#     morse_code = ''
#     for char in text.upper():
#         if char in MORSE_CODE_DICT:
#             morse_code += MORSE_CODE_DICT[char] + ' '
#         else:
#             morse_code += ' '
#     return morse_code.strip()
#
# # Example
# input_text = "My name is Aditya Vijay"
# morse_result = text_to_morse(input_text)
# print(f"The Morse code for '{input_text}' is: {morse_result}")




# Teacher
#
# class Teacher:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.__salary = salary  # Private attribute using double underscore
#
#     def get_salary(self):
#         """Provides controlled access to the private salary attribute."""
#         return self.__salary
#
#     def get_details(self):
#         """Provides formatted information about the teacher, excluding salary."""
#         return f"Name: {self.name}, Age: {self.age}"
#
# # Create a Teacher object
# teacher1 = Teacher("John Doe", 35, 50000)
#
# # Accessing public attributes
# print(teacher1.name)  # Output: John Doe
# print(teacher1.age)  # Output: 35
#
# # Accessing private attribute using the getter method
# print(teacher1.get_salary())  # Output: 50000
#
# # Attempting to access private attribute directly results in an error
# try:
#     print(teacher1.__salary)
# except AttributeError as e:
#     print("Error:", e)  # Output: Error: 'Teacher' object has no attribute '__salary'
#
# # Accessing other information using the public method
# print(teacher1.get_details())  # Output: Name: John Doe, Age: 35



























# MARATHON QUES 1
# def ODD(n):
#     matrix = [[0 for x in range(n)] for y in range(n)]
#
#     # initialize position of 1
#     r = n // 2
#     c = n - 1
#
#     # Filling the matrix by placing values
#     num = 1
#     while num <= (n * n):
#         if r == -1 and c == n:  # 3rd condition
#             c = n - 2
#             r = 0
#         else:
#             if c == n:
#                 c = 0
#             if r < 0:
#                 r = n - 1
#
#         if matrix[int(r)][int(c)]:  # 2nd condition
#             c = c - 2
#             r = r + 1
#             continue
#         else:
#             matrix[int(r)][int(c)] = num
#             num = num + 1
#
#         c = c + 1
#         r = r - 1  # 1st condition
#
#     # Printing matrix
#     print("N =", n)
#     print("Sum of each row, column and diagonal is: ",
#           n * (n * n + 1) // 2, "\n")
#
#     for i in range(0, n):
#         for j in range(0, n):
#             print('%2d ' % (matrix[i][j]),
#                   end='')
#
#             # To display output in matrix form
#             if j == n - 1:
#                 print()
#
#
# n=int(input("Enter Odd Number: "))
# ODD(n)








# MARATHON QUES 2
# class FrenchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'
#
#     class Card:
#         def __init__(self, rank, suit):
#             self.rank = rank
#             self.suit = suit
#
#         def __repr__(self):
#             return f"Card(rank='{self.rank}', suit='{self.suit}')"
#
#     def __init__(self):
#         self.cards = [self.Card(rank, suit) for suit in self.suits.split() for rank in self.ranks]
#
#     def __len__(self):
#         return len(self.cards)
#
#     def __getitem__(self, position):
#         return self.cards[position]
#
# # Example usage
# deck = FrenchDeck()
#
# # Fetch the first card in the deck
# print(deck[0])  # Output: Card(rank='2', suit='spades')
#
# # Fetch the last card in the deck
# print(deck[-1])  # Output: Card(rank='A', suit='hearts')
# print(deck[6])




# OR


# class FrenchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'
#
#     class Card:
#         def __init__(self, rank, suit):
#             self.rank = rank
#             self.suit = suit
#
#         def __repr__(self):
#             return f"Card(rank='{self.rank}', suit='{self.suit}')"
#
#
#
#     def __len__(self):
#         self.cards = [self.Card(rank, suit) for suit in self.suits.split() for rank in self.ranks]
#         return len(self.cards)
#
#     def __getitem__(self, position):
#         self.cards = [self.Card(rank, suit) for suit in self.suits.split() for rank in self.ranks]
#         return self.cards[position-1]
#
#
# deck = FrenchDeck()
#
# # Fetch the first card in the deck
# print(deck[0])
#
# # Fetch the last card in the deck
# print(deck[-1])
# print(deck[15])



# OR
# Question 2
# class FrenchDeck:
#     def __init__(self):
#         self.deck = []
#         self.rank = [str(n) for n in range(2, 11)] + list('JQKA')
#         self.suit = ["spades", "diamonds", "club", "hearts"]
#
#     def adding(self):
#         for i in self.suit:
#             for j in self.rank:
#                 self.deck.append((j, i))
#         return self.deck
#
#     def __getitem__(self, n):
#         return self.deck[n]
#
#     def __len__(self):
#         return len(self.deck)
#
#
# Taash = FrenchDeck()
# Deck = Taash.adding()
#
# #  Fetch the length of cards
# print(len(Deck))
#
# # Fetch the first card in the deck
# print(Deck[0])
#
# # Fetch the last card in the deck
# print(Deck[-1])
#
# # Fetch the random card in the deck
# print(Deck[:7])
#
#
#
#
#







# st = ["India is great", "Mera bharat mahan", "go india go", "the quick brown fox jumps over the lazy dog",
#       "run micheal run", "good blood bas blood"]
#
# for i in st:
#     res = i.split(" ")
#     if (res[::-1] == res):
#         print(f"{i} is Palindrome")
#     else:
#         print(f"{i} is not Palindrome")




#
# p1 = {"hello": "namaskar", "thank you": "shukriyad"}
# p2 = {"namaskar": "hello", "shukriyad": "thank you"}
# a = ''
# while a != 'bye':
#     a = input("Enter your text: ")
#
#     if a in p1.keys():
#         print(p1[a])
#
#     if a in p2.keys():
#         print(p2[a])








# Ques: Write a code to find how many times each character occurs in the string, put it in a dictonary.
# st= "abacaaabbbccddabbccabaddd"
# letter={}
# for i in st:
#     if i in letter:
#         letter[i]+=1
#     else:
#         letter[i]=1
# print(letter)
#
#
# # OR
#
# import collections
# st= "abacaaabbbccddabbccabaddd"
# res=collections.Counter(st)
# print(res)


# import sys
# for pth in sys.path:
#     print(pth)










#
# # REGULAR EXPRESSION
# # match, search, findall, finditer, compile, sub,
# import re
# st="this is a sample string"
# print(st)
#
# if re.match(r"^this",st):
#     print("Match found.\n")
# else:
#     print("Match not found.\n")
#
# if re.match(r"string",st):                           #match will search from starting and search will find in whole string
#     print("Match found.\n")
# else:
#     print("Match not found.\n")
#
# if re.search(r"string",st):
#     print("Match found.\n")
# else:
#     print("Match not found.\n")


# import re
# st="hello bat"
# res=re.search(r'b.t',st)     #one dot for single character and two dots for double character
#
# if res:
#     print("Match found")
#     print(res.group(0))        #string that matched the regex
# else:
#     print("Not found")


# import re
# st="bt"
#
# res=re.search(r'ba*t',st)      #here * means zero or more so a may not be present or upto any number.
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("Not found")


# import re
# st="baaaaaaaat"
#
# res=re.search(r'ba?t',st)      #here ? means 0 or 1 occurance.
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("Not found")



# import re
# st="bt"
#
# res=re.search(r'ba+t',st)      #here + means 1 or more occurance.
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("Not found")

#
# import re
# st="baaaaaaat"
#
# res=re.search(r'ba{3}t',st)      #here means exactly three times.
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("Not found")


# import re
# st="baaaaaaat"
#
# res=re.search(r'ba{3,}t',st)      #here means minimum three times.
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("Not found")



# import re
# st="b5t"
#
# res=re.search(r'b[a-zA-Z0-9]t',st)      #here means between a to z, A to Z and 0 to 9.
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("Not found")




#
# import re
# st="bait"
#
# res=re.search(r'b(oa|ai)t',st)      #here means oa or ai then boat or bait
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("Not found")





# import re
# st="bbt"
#
# # res=re.search(r'b[aeiou]t',st)      #here means vovel in between
# res=re.search(r'b[^aeiou]t',st)      #here means vovel in between zero or more
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("Not found")




#
# import re
# st="sample.py"
#
# res=re.search(r'\.py$',st)      #\ here means suppressing
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("Not found")










# ASSIGNMENT
# License Number
# LCNO-KAR-05-2014-0005
# LCNO- no change
# KAR-KER,APN,TND,TEL,MAH
# 05-RTO office number - 01-73 (no 00)
# 2014-2000+
# 0005-0001-9999 (no 0000)
# import re
# st="LCNO-KAR-05-2014-0005"                01-69   | 10,20,30,40,50,60,70-73              ?!0000[0-9]{4}
# rt = r"LCNO- (KAR|KER|APN|TND|TEL|MAH) - ([0-6][1-9]|[1-7][0-3])        -      2[0-9]{3} - (?!0000)[0-9]{4}"
# res = re.search(r'LCNO-(KAR|KER|APN|TND|TEL|MAH)-([0-6][1-9]|[1-7][0-3])-(2[0-9]{3})-((?!0000)[0-9]{4})', st)
# OR
# res = re.search(r'LCNO-(KAR|KER|APN|TND|TEL|MAH)-([0-6][1-9]|[1-7][0-3])-(2\d{3})-((?!0000)[0-9]{4})', st)
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("Not found")



# import re
# st="the quick brown fox jumps over the lazy dog"
# res=re.search(r'\w+',st)
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("match not found")

# import re
# st="the @#$ ^% quick brown fox jumps over the lazy dog"
# res=re.search(r'\W+',st)
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("match not found")

# import re
# st="123the quick brown fox jumps over the lazy dog  @!#$$#@#$ 13256"
# res=re.search(r'\D+',st)
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("match not found")

# import re
# st="the quick brown fox jumps over the lazy dog"
# res=re.search(r'\s+',st)
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("match not found")

# import re
# st="the@#$#@ quick brown fox jumps over the lazy dog"
# res=re.search(r'\S+',st)
#
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("match not found")



# import re
# st="asTor tHe quick brown fox jumps over the lazy dog"
# # res=re.search(r'(t\w+)',st,re.I)   #re.I means ignorance # in this it will give Tor as output as it will find substring
# # res=re.search(r'\b(t\w+)',st,re.I)   # here there is boundary, output will tHe.
# res=re.search(r'\B(t\w+)',st,re.I)
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("match not found")
#
#


# import re
#
# st = "tHe quick brown fox jumps over the lazy dog"
#
# res = re.search(r'\Athe', st, re.I)
# res = re.search(r'dog\Z', st, re.I)
# if res:
#     print("Match found")
#     print(res.group(0))
# else:
#     print("match not found")



# BACK TRACKING


# import re
#
# st = "good blood bad blood"
#
# res = re.search(r'(\w+)\s(\w+)\s(\w+)\s(\2)', st, re.I)
# if res:
#     print("Match found")
#     print(res.group(0))
#     print(res.group(1))
#     print(res.group(2))
#     print(res.group(3))
#     print(res.group(4))
# else:
#     print("match not found")
#




# Assignment 2
# Valid
# dd\mm\yyyy
# dd-mm-yyyy
# Not Valid
# dd\mm-yyyy
# dd-mm\yyyy

# dd-> 01-31
# mm-> 01-12
# yyyy-> 1900+

# import re
# st = "31/02/2024"
# #                    01- 29     10,20,30,31  \ -      01-09 10-12   \ -      1900-1999 2000-2999
# res = re.search(r'([0-2][1-9]|[1-3][0-1])(/|-)(0[1-9]|1[0-2])(\2)(19\d{2}|\d{4})',st)
# if res:
#     print("date found")
#     print(res.group(0))
# else:
#     print("date not found")
#     # print(res.group(0))



# Very very Important
# import re
# st="the quick brown fox jumps over the lazy dog fox fox fox fox"
# res=re.search(r'fox',st)

# if res:
#     print("Match found")
#     print("rejected string : ",st[:res.start()])
#     print(res.group(0))
#     print("unchecked string : ", st[res.end():])
# else:
#     print("match not found")

# res2 = re.search(r"fox", st[res.end():])
# if res2:
#     print(res2.group(0))
# else:
#     print(False)

# count = 0
# for match in re.finditer(r"fox", st):
#     count += 1
#     print("match", count, match.group(), "start index", match.start(), "End index", match.end())

# How to iterate in match means to find the occurrence of word in the given string





#Findall
# import re
# st="""
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# """
# regex=re.compile(r'(t\w+)')  #Compile convert the string into regex expression, We can do the same code without using compile method
# res=re.findall(regex,st)
# print(res)
# print(res.count('the'))


# #finditer
# import re
# st="""
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# the quick brown fox jumps over the lazy dog
# """
# for match in re.finditer(r'(t\w+)',st):
#     s=match.start()
#     e=match.end()
#     print(s,"-",e,"-", st[s:e])



# Sub


# import re
# st="the quick brown fox jumps over the lazy dog"
# res=re.sub(r'(t\w+)',"The",st,count=1) #if we remove count then it will change all the similar string, but here only 1st string.
# print(res)
#
# res=re.sub(r'fox',"tiger",st,count=1)
# print(res)



# import re
# f=open("stories.txt","rb")
# st=str(f.read())
# rstart=re.compile(r'(t\w+)')
# # rend=re.compile(r'(\w+e)')
# res=re.findall(rstart,st)
# print(res)
# # res1=re.findall(rend,st)
# # print(res1)
# f.close()
print("hello ")