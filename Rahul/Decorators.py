# # find out the execution time of a function using a decorator.
#
# # importing libraries
# import time
# import math
#
#
# # decorator to calculate duration
# # taken by any function.
# def calculate_time(func):
#     # added arguments inside the inner1,
#     # if function takes any arguments,
#     # can be added like this.
#     def inner1(*args, **kwargs):
#         # storing time before function execution
#         begin = time.time()
#
#         func(*args, **kwargs)
#
#         # storing time after function execution
#         end = time.time()
#         print("Total time taken in : ", func.__name__, end - begin)
#
#     return inner1
#
#
# # this can be added to any function present,
# # in this case to calculate a factorial
# @calculate_time
# def factorial(num):
#     # sleep 2 seconds because it takes very less time
#     # so that you can see the actual difference
#     time.sleep(2)
#     print(math.factorial(num))
#
#
# # calling the function.
# factorial(10)
#
#
#
#
#
#
#
#
# # Chaining Decorators
#
# # code for testing decorator chaining
# def decor1(func):
#     def inner():
#         x = func()
#         return x * x
#
#     return inner
#
#
# def decor(func):
#     def inner():
#         x = func()
#         return 2 * x
#
#     return inner
#
#
# @decor1
# @decor
# def num():
#     return 10
#
#
# @decor
# @decor1
# def num2():
#     return 10
#
#
# print(num())
# print(num2())
#
#
#
#
#
#
#
#
#












# # # Cheat-Sheet
# # 1. Basics:

# # Decorator Syntax:


# @decorators
# def function():
#     pass

# # Equivalent to:
# def function():
#     pass
# function = decorator(function)

# # 2. Defining Decorators:

# # Without Arguments:
# def simple_decorator(func):
#     def wrapper():
#         # Do something before
#         result = func()
#         # Do something after
#         return result
#     return wrapper


# # With Arguments:
# def decorator_with_args(arg):
#     def wrapper(func):
#         def inner_wrapper(*args, **kwargs):
#             # Do something with arg
#             result = func(*args, **kwargs)
#             return result
#         return inner_wrapper
#     return wrapper


# # 3. Applying Decorators:

# # On Functions:
# @simple_decorator
# def hello():
#     print("Hello, world!")

# # On Methods:
# class MyClass:
#     @simple_decorator
#     def method(self):
#         print("Method called")


# # 4. Common Use Cases:

# # Logging:
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function {func.__name__} with args {args} and kwargs {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Function {func.__name__} returned {result}")
#         return result
#     return wrapper

# # Timing:
# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
#         return result
#     return wrapper

# # 5. Chaining Decorators:

# @log
# @timer
# def my_function():
#     pass

# # Equivalent to:
# my_function = log(timer(my_function))

# # 6. Preserving Metadata:

# import functools

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         pass
#     return wrapper


# # 7. Class-based Decorators:

# class Decorator:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         # Do something before
#         result = self.func(*args, **kwargs)
#         # Do something after
#         return result
