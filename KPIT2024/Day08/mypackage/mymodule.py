
gname = "Sachin Tendulkar"

sports = ['cricket', 'football', 'hockey', 'baseball', 'swimming']

runs = {'test': 18500, 'ODI': 14200, 't20': '2300'}

def greet(guest):
    print(f"Greeting Mr.{guest}, Welcome to the event....")


class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    # print(__name__)

    print("-" * 60)

    greet("Virat Kholi")

    print("-" * 60)

    ply1= Player("Sehwag", 36)
    ply1.get_details()
    print("-" * 60)