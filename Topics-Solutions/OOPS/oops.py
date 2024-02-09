# # # Animal 
# class Animal:
#     species = "Unknown"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         pass

#     def describe(self):
#         return f"{self.name} is {self.age} years old and is a {self.species}."


# class Dog(Animal):
#     species = "Canine"

#     def make_sound(self):
#         return "Woof!"


# class Cat(Animal):
#     species = "Feline"

#     def make_sound(self):
#         return "Meow!"

#     def describe(self):  # Method overriding
#         return f"{self.name} is {self.age} years old and is a {self.species}. Also, cats rule!"


# class Bird(Animal):
#     species = "Avian"

#     def make_sound(self):
#         return "Chirp!"


# def get_animal_details():
#     name = input("Enter the name of the animal: ")
#     age = int(input("Enter the age of the animal: "))
#     return name, age


# # Create instances of different animals using user input
# dog_name, dog_age = get_animal_details()
# dog = Dog(dog_name, dog_age)

# cat_name, cat_age = get_animal_details()
# cat = Cat(cat_name, cat_age)

# bird_name, bird_age = get_animal_details()
# bird = Bird(bird_name, bird_age)

# # Call methods and describe animals
# print(dog.make_sound())  # Output: Woof!
# print(cat.make_sound())  # Output: Meow!
# print(bird.make_sound())  # Output: Chirp!

# print(dog.describe())  # Output: Buddy is 3 years old and is a Canine.
# print(cat.describe())  # Output: Whiskers is 5 years old and is a Feline. Also, cats rule!
# print(bird.describe())  # Output: Polly is 2 years old and is a Avian.











# 1. Bank Account Management System with User Inputs:

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance


# Get user inputs
account_number = input("Enter account number: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(account_number, initial_balance)

# Perform transactions
amount_to_deposit = float(input("Enter amount to deposit: "))
account.deposit(amount_to_deposit)

amount_to_withdraw = float(input("Enter amount to withdraw: "))
account.withdraw(amount_to_withdraw)

print("Account balance:", account.get_balance())









# 2. Employee Management System with User Inputs:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: ${self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"Name: {self.name}, Salary: ${self.salary}, Department: {self.department}"


# Get user inputs
employee_name = input("Enter employee name: ")
employee_salary = float(input("Enter employee salary: "))
employee = Employee(employee_name, employee_salary)

manager_name = input("Enter manager name: ")
manager_salary = float(input("Enter manager salary: "))
manager_department = input("Enter manager department: ")
manager = Manager(manager_name, manager_salary, manager_department)

# Display details
print("Employee details:", employee.get_details())
print("Manager details:", manager.get_details())










# 3. Shape Hierarchy with User Inputs:

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Get user inputs
circle_radius = float(input("Enter radius of the circle: "))
circle = Circle(circle_radius)

rectangle_width = float(input("Enter width of the rectangle: "))
rectangle_height = float(input("Enter height of the rectangle: "))
rectangle = Rectangle(rectangle_width, rectangle_height)

# Display calculations
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())










# 1. Library Management System:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if self.books:
            for i, book in enumerate(self.books, start=1):
                print(f"Book {i}: {book.display_info()}")
        else:
            print("No books available in the library.")


# Create library instance
library = Library()

# Add books
num_books = int(input("Enter the number of books to add: "))
for i in range(num_books):
    title = input(f"Enter title of book {i+1}: ")
    author = input(f"Enter author of book {i+1}: ")
    book = Book(title, author)
    library.add_book(book)

# Display books
print("\nLibrary books:")
library.display_books()










# 2. Student Management System:

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if self.students:
            for i, student in enumerate(self.students, start=1):
                print(f"Student {i}: {student.display_info()}")
        else:
            print("No students enrolled in the school.")


# Create school instance
school = School()

# Add students
num_students = int(input("Enter the number of students to add: "))
for i in range(num_students):
    name = input(f"Enter name of student {i+1}: ")
    age = int(input(f"Enter age of student {i+1}: "))
    grade = input(f"Enter grade of student {i+1}: ")
    student = Student(name, age, grade)
    school.add_student(student)

# Display students
print("\nSchool students:")
school.display_students()










# 3. Product Inventory Management System:

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return f"Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        if self.products:
            for i, product in enumerate(self.products, start=1):
                print(f"Product {i}: {product.display_info()}")
        else:
            print("No products available in the inventory.")


# Create inventory instance
inventory = Inventory()

# Add products
num_products = int(input("Enter the number of products to add: "))
for i in range(num_products):
    name = input(f"Enter name of product {i+1}: ")
    price = float(input(f"Enter price of product {i+1}: "))
    quantity = int(input(f"Enter quantity of product {i+1}: "))
    product = Product(name, price, quantity)
    inventory.add_product(product)

# Display products
print("\nInventory products:")
inventory.display_products()
