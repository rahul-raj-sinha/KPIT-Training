
class Player:

    def __init__(self):
        self.name = "Sachin"
        self.age = 36

    def get_details(self):
        print(f"The name is {self.name}\n age is {self.age}")

sachin = Player()
sachin.get_details()

rahul = Player()
rahul.get_details()
rahul.name = "Dravid"
rahul.age = 32

print(rahul.get_details())
