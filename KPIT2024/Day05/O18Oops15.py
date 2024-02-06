
class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.age = 1
    def eat(self):
        print("Animals eat.....")


class Bird(Animal):

    def __init__(self):
        super().__init__()              # parent class constructor
        print("Bird Ctor......")
        self.weight = '1 kg'


    def fly(self):
        print("Birds Fly......")

cuckoo = Bird()
cuckoo.fly()

print(cuckoo.__dict__)