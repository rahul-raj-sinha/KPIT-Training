
class Player:

    def __init__(self):             # constructor
        print("Player Initialized")

    def get_runs(self):
        print("Runs Scored........")

    def __del__(self):
        print("Object Deleted.....")

sachin = Player()           # calls the constructor
sourav = Player()
sachin.__init__()

sachin.get_runs()
sourav.get_runs()

del sachin
print("Hello World")
