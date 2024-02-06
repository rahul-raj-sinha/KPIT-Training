
class Player:

    def __init__(self, name, age):
        self.name =name
        self.age = age

    def get_details(self):
        print(f"The name is {self.name}\n age is {self.age}")


ply1 = Player('Sachin', 36)
ply2 = Player("Sourav", 35)

print("-" * 60)

ply1.get_details()
ply2.get_details()

ply1.name = "Sachin Tendulkar"
print("-" * 60)

print(ply1.__dict__)
print(ply2.__dict__)

print("-" * 60)
ply2.runs = 150
print(ply2.__dict__)
print(ply1.__dict__)
