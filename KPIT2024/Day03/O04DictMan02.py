
player = {'name': 'Rahul', 'age': 32, 'runs': 150, 'oppn': 'SA' }
print(f"player :{player}")

print("-" * 60)
#Get
print("Name :", player.get('name', "Please enter a proper key"))
print("Age  :", player.get('ae', "Please enter a proper key"))

print("-" * 60)

print(f"player :{player}")
# keys

k = player.keys()
print(k)

print()
for k in player.keys():
    print(k, "=>", player[k])

print("-" * 60)

print(f"player :{player}")
# values

v = player.values()
print(f"values :{v}")

print("-" * 60)
# fromkeys - converting a list into a dictionary (key)

cities = ['blr', 'che', 'mum', 'del', 'hyd', 'kol']
print(f"cities :{cities}")
print(type(cities))

dct01 = dict.fromkeys(cities)
print(f"dct01 :{dct01}")

dct02 = dict.fromkeys(cities, 23)
print(f"dct01 :{dct02}")

print("-" * 60)
# setdefault - if want to add new key values into the dictionary

stud = {'name': 'Jack', 'age': 12, 'class': 7}
print(f"stud :{stud}")

# modifying the keys that are already existing
stud.setdefault('name', 'Mike')
stud.setdefault('class', '5')

# adding a new key value
stud.setdefault('school', 'NPS')
stud.setdefault('Loc', 'Jaynagar')

print(f"stud :{stud}")
