class Employee:

    def __init__(self, name):
        self.name = name
        self.tech = ['C', 'C++', 'Java', 'Spring', 'Hibernate', 'Angular']

    def  __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, ind, val):
        self.tech[ind] = val


emp1 = Employee("Jack")

print([x for x in emp1])
print("-" * 60)

emp1.append("Python")
print([x for x in emp1])
print("-" * 60)

x = emp1[0]
print(x)
print("-" * 60)

emp1[4] ="ReactJS"
print([x for x in emp1])