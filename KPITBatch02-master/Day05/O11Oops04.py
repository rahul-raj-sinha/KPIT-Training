
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 35)
ply1.get_details()

print("-" * 60)
ply2 = Player("Rahul", 34)
ply2.get_details()

print("-" * 60)
ply2.age = 40
ply2.get_details()


print("-" * 60)
ply1.get_details()




