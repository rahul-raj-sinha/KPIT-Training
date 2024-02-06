
class Animal:

    def __init__(self):
        print("Animal Ctor")
        self.a = 10

    def eat(self):
        print("Animals eat......")

    def fun(self):
        print("fun of Animal Class......")

class Person:

    def __init__(self):
        print("Person Ctor....")
        self.p = 20

    def Talk(self):
        print("Person Talk.....")

    def fun(self):
        print("Fun of person class......")


class Girl(Animal, Person):

    def __init__(self):
        super().__init__()          # parent class
        Person.__init__(self)
        print("Girl Ctor.....")
        self.g = 30

    def Walk(self):
        print("Girls Walk......")


print("-" * 60)
gracy = Girl()
gracy.fun()



print("-" * 60)
gracy.Walk()
gracy.Talk()
gracy.eat()

print("-" * 60)
print(gracy.__dict__)