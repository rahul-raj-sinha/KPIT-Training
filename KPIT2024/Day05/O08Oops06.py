import datetime


class Player:

    def __init__(self, name , age):
        # print(  ....")
        self.name = name
        self.age = age


    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    # @classmethod
    # def createPlayer(cls, fn, ln, age):
    #     print("factory.....")
    #     return cls(f"Mr.{fn} {ln}", age)               # will call the constructor
    from datetime import date
    @classmethod
    def createPlayer(cls,fn,dob):
        d1 = datetime.date.today()
        d2 = dob.strftime("%d/%m/%Y")
        age = d2-d1
        return cls(fn,age)

ply1 = Player("Sachin", 36)
ply1.get_details()

print("-" * 60)

# ply2 = Player.createPlayer("Rahul", "Dravid", 32)
# ply2.get_details()

ply3 = Player.createPlayer("Virat","15/11/1989")
ply3.get_details()
