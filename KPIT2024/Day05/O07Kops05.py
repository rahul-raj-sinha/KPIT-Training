
class Player:

    team = "India"              # class Attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_details(self):
        print(f"The name is {self.name}\n age is {self.age}")


ply1 = Player("Sachin", 36)
ply2 = Player("Rahul", 32)

print(f"ply1 :{ply1.team}")
print(f"ply2 :{ply2.team}")
print(f"Player :{Player.team}")

print("-" * 60)
Player.team = "Mumbai Indians"

print(f"ply1 :{ply1.team}")
print(f"ply2 :{ply2.team}")
print(f"Player :{Player.team}")

print("-" * 60)
ply2.team = "RCB"
print(f"ply2 :{ply2.team}")

print("-" * 60)
print(f"ply1 :{ply1.team}")
print(f"Player :{Player.team}")

print("-" * 60)
print(ply2.__dict__)
print(ply1.__dict__)    

print("-" * 60)
print(Player.__dict__)