

from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    # The same works for not equal alsse
    def __eq__(self, other):
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee("Peter", 75000)
emp2 = Employee("Richard", 80000)

print("-" * 60)
print(emp1)

print("-" * 60)
print(emp2)

print("-" * 60)
if (emp1 == emp2):
    print(f"{emp1.name}'s Salary {emp1.salary} is equal to {emp2.name}'s salary of {emp2.salary}")
else:
    print(f"{emp2.name}'s Salary {emp1.salary} is not equal to {emp1.name}  salary of {emp1.salary}")

if (emp1 != emp2):
    print(f"{emp1.name}'s Salary {emp1.salary} is not equal to {emp2.name}'s salary of {emp2.salary}")
else:
    print(f"{emp2.name}'s Salary {emp1.salary} is equal to {emp1.name}  salary of {emp1.salary}")

print("-" * 60)

if emp1 > emp2:
    print(f"{emp1.name}'s Salary {emp1.salary} is Less than  {emp2.name}'s salary of {emp2.salary}")
else:
    print(f"{emp1.name}'s Salary {emp1.salary} is not less than  {emp2.name}'s salary of {emp2.salary}")


if emp1 < emp2:
    print(f"{emp1.name}'s Salary {emp1.salary} is greater than  {emp2.name}'s salary of {emp2.salary}")
else:
    print(f"{emp1.name}'s Salary {emp1.salary} is not greater than  {emp2.name}'s salary of {emp2.salary}")


print("-" * 60)
print(emp1 >= emp2)

# overload == and one more operator

