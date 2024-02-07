
class Player:

    def __init__(self, name, age):
        print("Ctor called.....")
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def CreatePlayer(cls, fname, lname, age):
        print(f"factory......")
        # calls the constructor
        return cls(f"{fname} {lname}", age)


ply1 = Player("Sachin", 37)
ply1.get_details()

print("-" * 60)

ply2 = Player.CreatePlayer("Virat","Kholi", 36)
ply2.get_details()
