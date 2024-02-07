
gname = 'Sachin Tendulkar'

sports = ['cricket', 'hockey', 'football', 'tennis', 'badmiton', 'basketball', 'swimming']

runs = {'test': 16500, 'odi': 12000, 't20': 2500}

def greet(guest):
    print("-" * 60)
    print(f"Greetings Mr.{guest}, Welcome to the event.......")
    print("-" * 60)

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_details(self):
        print(f"Name is {self. name}\nAge is {self.age}")
        print("-" * 60)

# ---------------------------------------------
print(__name__)

if __name__ == '__main__':
    greet("Abhishek")

    ply1 = Player('Vijay', 20)
    ply1.get_details()
