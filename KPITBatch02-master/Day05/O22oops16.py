
class Animal:

    def __init__(self):
        print("Animal Ctor....")
        self.age = 1

    def eat(self):
        print("animals eat......")

class Bird(Animal):

    def fly(self):
        print("Birds fly.....")

class Fish(Animal):

    def swim(self):
        print("Fishes swim......")


cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 60)
dolphin = Fish()
dolphin.eat()
dolphin.swim()

print("-" * 60)
print(cuckoo.__dict__)
print(dolphin.__dict__)

