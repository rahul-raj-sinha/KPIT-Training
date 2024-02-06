
class Player:           # pascal casing

    def get_runs(self):
        print("Runs Scored....")
        print(self.__class__)


sachin = Player()           # calls the default constructor
sachin.get_runs()
print(type(sachin))

print("-" * 60)
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance("sachin", str))