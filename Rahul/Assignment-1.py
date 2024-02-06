'''
Q1 Pattern
1
23
456
7890
'''
# num=1
# for i in range(0,5):
#     for j in range(0,i):
#         if num==10:
#             print(0)
#             break
#         print(num, end=" ")
#
#
#         num+=1
#     print("\r")
#
#
#
# print("-"*60)
'''
Q Pattern
 1 2 3 4 5
  1 2 3 4
   1 2 3
    1 2
     1
    2 1
   3 2 1
  4 3 2 1
 5 4 3 2 1
'''
# for i in range(1,6):
#     print()
#     print(" "*i, end=" ")
#     for j in range(1,7-i):
#         print(j,end=" ")
#
# k=2
# while k<6:
#     print()
#     print(" "*(6-k), end=" ")
#     for l in range(k,0,-1):
#         print(l,end=" ")
#     k+=1
#
#
#
# print("-"*60)
'''
Q Pattern
1
22
333
4444
55555
'''
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i, end="")
#     print('\r')


# print("-" * 60)
'''
Q Pattern
        1
       1 2
      1 2 3
     1 2 3 4
    1 2 3 4 5
     1 2 3 4
      1 2 3
       1 2
        1
'''
# for i in range(1,6):
#     digit=1
#     for j in range(6,0,-1):
#         if j>i:
#             print(" ", end='')
#         else:
#             print(digit,end=' ')
#             digit+=1
#     print("")
#
#
# for i in range(4, 0, -1):
#
#         print(" " * (5 - i), end=' ')
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()


# print("-" * 60)
# Q2 Prime number b/w 50 to 150 and the count of it.
# count=0
# for i in range(50,151):
#         if i>1:
#             for j in range(2,i):
#                 if(i%j)==0:
#                     break
#             else:
#                 print(i)
#                 count+=1
# print(f"Numbers of Prime Numbers between 50 to 150 : {count}" )
#
#
#
#
#
# print("-"*60)
# Q3  write a code to generate fibonacci series
# n = int(input("Enter Number : "))
# a = 0
# b = 1
# if n == 0:
#     print(0)
# for i in range(2, n):
#     print(a)
#     c = a + b
#     a = b
#     b = c
# print(b)
#
# print("-" * 60)

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


'''
4. write a code to find the next number

     1=1!
     2=2!
    145=1!+4!+5!
    	1 + 24 + 120
	145

what is the next number that satisfies this condition
'''


# def Fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * Fact(n - 1)
#
#
# num = input("Enter number: ")
# result = 0
# for i in range(len(num)):
#     result = result + Fact(int(num[i]))
# if result == int(num):
#     print("Correct")
# else:
#     print("Not Correct")

# print("-" * 60)

# 5. write a code to generate armstrong series

# def armstrong(n):
#     l = len(str(n))
#     temp = n
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** l
#         temp //= 10
#     return sum
#
#
# n = int(input("Enter Number : "))
# result = armstrong(n)
# if result:
#     print("Yes Armstrong")
# else:
#     print("No Armstrong")

# print("-" * 60)



# Sort the month based on calender
# from calendar import month_abbr
# a=list(month_abbr)
# print(a)
# months=['apr','aug','dec','feb','mar','may','nov','oct','jan','jun','jul','sep']
# b=sorted(months,key=list(map(lambda month: month.lower(), list(month_abbr))).index)
# print(b)





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

# 6.Calculate the area of a rectangle given its length and width.
# def area(l,b):
#     return l*b
# n=int(input("Length : "))
# m=int(input("breadth : "))
# result=area(n,m)
# print(result)


# print("-" * 60)
# 7.Convert a temperature from Celsius to Fahrenheit using the formula: F = (C * 9/5) + 32.
# def CtoF(c):
#     return (c * (9 / 5)) + 32
#
#
# c = int(input("Celsius: "))
# result = CtoF(c)
# print(result)


# print("-" * 60)
# 8.Calculate the area of a circle given its radius using the formula: A = π * r^2.

# def Area(r):
#     return (3.14*(r**2))
#
#
# r = int(input("radius: "))
# result = Area(r)
# print(result)


# print("-" * 60)
# 9.Compute the hypotenuse of a right triangle using the Pythagorean theorem: c = sqrt(a^2 + b^2).

# import math
# def hypotenuse(a,b):
#     return (math.sqrt((a**2)+(b**2)))
#
#
# a = int(input("a: "))
# b = int(input("b: "))
# result = hypotenuse(a,b)
# print(result)

# print("-" * 60)
# 10.Calculate the simple interest on an investment using the formula: A = P * T * R / 100;


# print("-" * 60)
# 11.Calculate the compound interest on an investment using the formula: A = P * (1 + r/n)^(n*t).
# def CI(P,r,n,t):
#     return (P*(1+(r/n))**(n*t))
#
#
# P = int(input("P: "))
# r = int(input("r: "))
# n = int(input("n: "))
# t = int(input("t: "))
# result = CI(P,r,n,t)
# print(result)


# print("-" * 60)
# 12.Determine the volume of a sphere given its radius using the formula: V = (4/3) * π * r^3.
# def Volume(r):
#     return ((4/3)*3.14*(r**3))
#
#
#
# r = int(input("r: "))
#
# result = Volume(r)
# print(result)


# print("-" * 60)
# 13.Convert a distance from kilometers to miles using the formula: miles = kilometers * 0.621371.
# def DisToKilo(km):
#     return (km * 0.621371)
#
#
# km = int(input("km: "))
#
# result = DisToKilo(km)
# print(result)


# print("-" * 60)
# 14.Calculate the sum of the first n natural numbers using the formula: sum = (n * (n + 1)) / 2.
# def SumOfN(n):
#     return ((n*(n+1))/2)
#
#
# n = int(input("n: "))
#
# result = SumOfN(n)
# print(result)


# print("-" * 60)

# 15.Compute the area of a triangle given the lengths of its three sides using Heron's formula.
# The formula is as follows:

# s = (a + b + c) / 2
# A = sqrt(s * (s - a) * (s - b) * (s - c))

# where:
# a, b, and c are the lengths of the triangle's sides.
# s is the semiperimeter (half of the perimeter) of the triangle.
# A is the area of the triangle.

# import math
# def heronArea(a, b, c):
#     s = ((a + b + c) / 2)
#     A = (math.sqrt(s * (s - a) * (s - b) * (s - c)))
#     return A
#
#
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
#
# result = heronArea(a, b, c)
# print(result)

# print("-" * 60)

# Write program to find Palindrome
# def Palindrome(n):
#     temp = n
#     rev = 0
#     while (n != 0):
#         sum = (n % 10)
#         rev = rev * 10 + sum
#         n = n // 10
#     # print(temp,sum)
#     if (temp == rev):
#         return True
#     else:
#         return False
#
# n = int(input())
# if Palindrome(n):
#     print("Yes")
# else:
#     print("No")




# Write a program to find the sum of all odd numbers between 1 and 50

# def sumOfOdd(n):
#     sum=0
#     for i in range(1,n+1):
#
#         if(i%2 != 0):
#             sum=sum+i
#     return sum
# n=int(input())
# print(sumOfOdd(n))



# Write a program to find the sum of all even numbers between 1 and 50
# def sumOfOdd(n):
#     sum=0
#     for i in range(1,n+1):
#
#         if(i%2 == 0):
#             sum=sum+i
#     return sum
# n=int(input())
# print(sumOfOdd(n))


# Write a program to find the sum of squares of  even numbers between 1 and 50
# def sumOfOdd(n):
#     sum=0
#     for i in range(1,n+1):
#
#         if(i%2 == 0):
#             sum=sum+(i**2)
#     return sum
# n=int(input())
# print(sumOfOdd(n))



#Write a program to check if a given number is a perfect number.
# def sumOfOdd(n):
#     sum=0
#     for i in range(1,n):
#
#         if(i%2 == 0):
#             sum=sum+i
#         if sum==n:
#             return True
# n=int(input())
# if sumOfOdd(n):
#     print("Yes")
# else:
#     print("No")


#Write a program to print the ASCII values of all uppercase alphabets.
# alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# for i in alphabet:
#      k=ord(i)
#      print(f" The value of {i} is - {k}")

# Write a program to reverse a given number.
# n=(input())
# b=n[::-1]
# print(b)




# Write a program to find the greatest common divisor (GCD) and LCM of two numbers.

# def GCD(a,b):
#     hcf=0
#     small=0
#     if a>b:
#         small=b
#     else:
#         small=a
#     for i in range(1,small+1):
#         if a%i==0 and b%i==0:
#            hcf=i
#     return hcf
# def LCM(a,b,hcf):
#     return (a*b)/hcf
#
# a=int(input("enter a"))
# b=int(input("enter b"))
# c=GCD(a,b)
# d=LCM(a,b,c)
# print(c)
# print(int(d))




# Write a program to check if a given year is a leap year.
# def leap(a):
#     if (a%4==0 or (a%100!=0 and a%400==0)):
#         print("leap Year")
#     else:
#         print("Not leap Year")
# a=int(input())
# leap(a)




# Write a program to check if a given string is a pangram.
# def Pangram(a):
#     l=[]
#     for i in range(26):
#         l.append(False)
#     for c in a.lower():
#         if not c==" ":
#             l[ord(c) - ord('a')] = True
#     for ch in l:
#         if ch==False:
#             return False
#
#     return True
#
# a=input()
# if(Pangram(a)):
#     print("Yes")
# else:
#     print("No")

# OR


# import string
# def ispangram(str):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for char in alphabet:
#         if char not in str.lower():
#             return False
#
#     return True
#
#
# # Driver code
# string = 'the quick brown fox jumps over the lazy dog'
# if (ispangram(string) == True):
#     print("Yes")
# else:
#     print("No")


# Write a program to check if a given number is a perfect square.
# def per(n):
#     snum=int(n**0.5)
#     if snum**2==n:
#         print("Yes")
#     else:
#         print("No")
# n=int(input())
# per(n)


# Write a program to find the sum of the digits of a given number until the sum is a single digit.
# def digit(n):
#     sum=0
#     while (n>0 or sum>9):
#         if(n==0):
#             n=sum
#             sum=0
#         sum+=n%10
#         n//=10
#     return sum
# n=int(input())
# print(digit(n))