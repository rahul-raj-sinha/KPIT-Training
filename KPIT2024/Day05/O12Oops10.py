
class Employee:

    def __init__(self, name):
        self.__name = name                  # private Variable
        self.tech = ['C', 'C++', 'Java', 'Spring', 'Hibernate', 'Angular']

    def __str__(self):
        return self.__name + " - " + ", ".join([v for v in self.tech])


emp1 = Employee("Mike")
print(emp1)
