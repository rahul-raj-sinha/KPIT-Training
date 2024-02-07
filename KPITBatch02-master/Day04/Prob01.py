def fibonacci(n):
    if n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
num=int(input("Enter how many number to print:"))
for i in range(1,num+1):
    print(fibonacci(i),end=" ")