
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'Sachin', 'runs': 85, 'age': 32, 'oppn': 'Aus'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict({'bookid': 'B101', 'bookname': 'Learning Python', 'price': 750, 'publication': 'Orielly'})
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict([('name', 'Rahul'), ('age', 34), ('runs', 45), ('oppn', 'SA') ])
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
d5 = dict(name='Sourav', age=36, runs=60, oppn='Eng')
print(f"d5 :{d5}")
print(type(d5))

print("-" * 60)
# Create
player = {'name': 'Sachin', 'age': 34, 'runs': 98, 'oppn': 'WI'}
print(f"player :{player}")

print("-" * 60)
# read
print("Name :", player['name'])
print("Age  :", player['age'])
print("Runs :", player['runs'])

print("-" * 60)
for x in player:
    print(x + " => " + str(player[x]))

print("-" * 60)
# update - adding new elements, modifying
player['runs'] = 105
player['name'] = 'Tendulkar'
player['venue'] = 'sabina park'
player['year'] = 2002

print(f"player :{player}")

print("-" * 60)
# delete
del player['age']
del player['year']
print(f"player :{player}")

print("-" * 60)
print(dir(player))
