
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'Sachin', 'age': 34, 'runs': 85, 'oppn': "WI"}
print(f"d2: {d2}")
print(type(d2))

print("-" * 60)
d3 = dict({'name': 'Sachin', 'age': 34, 'runs': 85, 'oppn': "WI"})
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict([('name', 'sachin'), ('age', 34), ('runs', 125), ('oppn', 'Aus')])
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
d5 = dict(name="Sachin", age=35, runs=97, oppn="Pak")
print(f"d5 :{d5}")
print(type(d5))

print("-" * 60)
# create
player = {'name': 'sehwag', 'age': 34, 'runs': 85, 'oppn': "WI"}
print(f"player :{player}")

print("-" * 60)
# read
print(f"Name : {player['name']}")
print(f"Runs  :{player['runs']}")

print("-" * 60)
for i in player:
    # print(i, end=" ")
    print(i, "=>", player[i])

print("-" * 60)
#update
print(f"player :{player}")
player['loc'] = "Sabina Park"
player['year'] = 1998

print(f"player :{player}")

player['runs'] = 25
player['name'] = "VVS laxman"

print(f"player :{player}")

print("-" * 60)
#delete
print(f"player :{player}Pl")
del player['year']
del player["oppn"]

print(f"player :{player}")

print("-" * 60)
print(dir(d1))