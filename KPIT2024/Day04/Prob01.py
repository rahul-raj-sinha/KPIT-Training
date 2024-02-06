
# factorial of a number

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

num = int(input("Enter a number to find its factorial :"))
print(f"The factorial of num is :{fact(num)}")

print("-" * 60)

def fibo(x):
    if x <= 1:
        return x
    else:
        return fibo(x - 1) + fibo(x - 2)

iter = int(input("Enter the number of fibanocci series to be generated :"))
print("Fibonocci Series")
for i in range(iter):
    print(fibo(i), end=" ")
print()
