

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C', 'C++', 'Java', 'Spring', 'Hibernate', 'AngularJS']

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __len__(self):
        return len(self.tech)

    def __getitem__(self, idx):
        return self.tech[idx]

    def __setitem__(self, idx, val):
        self.tech[idx] = val


emp1  = Employee("David", 45000)
print(emp1)

print("-" * 60)
print([tech for tech in emp1])

print("-" * 60)
emp1.append("python")
print([tech for tech in emp1])

print("-" * 60)
print(len(emp1))

print("-" * 60)
tech1 = emp1[2]
print(tech1)

print("-" * 60)
emp1[5] = "ReactJS"

print("-" * 60)
print([tech for tech in emp1])
