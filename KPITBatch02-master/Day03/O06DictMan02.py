
player = {'name': 'Rahul', 'age': 31, 'runs': 65, 'oppn': 'Pak'}
print(f"player :{player}")

print("get".center(60, "-"))
print(player.get('opn', "Please check the key mentioned"))
print(player.get('oppn', "Please check the key mentioned"))

print("keys".center(60, "-"))
player = {'name': 'Rahul', 'age': 31, 'runs': 65, 'oppn': 'Pak'}
print(f"player :{player}")

k = player.keys()
print(f"keys :{k}")

for k in player.keys():
    print(k, "=>", player[k])

print("values".center(60, "-"))

player = {'name': 'Rahul', 'age': 31, 'runs': 65, 'oppn': 'Pak'}
print(f"player :{player}")
v = player.values()

print(f"values :{v}")

print("fromkeys".center(60, "-"))
cities = ['blr', 'che', 'mum', 'del', 'kol', 'hyd']
print(f"cities :{cities}")

res = dict.fromkeys(cities)
print(f"res :{res}")

res = dict.fromkeys(cities, 24)
print(f"res :{res}")

print("setdefault".center(60, "-"))

player = {'name': 'Rahul', 'age': 31, 'runs': 65, 'oppn': 'Pak'}
print(f"player :{player}")

player.setdefault('name', 'Dravid')
player.setdefault('age', 28)
player.setdefault('team', "India")
player.setdefault('venue', 'Chepauk')
print(f"player :{player}")

print("pop".center(60, "-"))
player = {'name': 'Rahul', 'age': 31, 'runs': 65, 'oppn': 'Pak', 'team': 'India', 'venue': 'Chepauk'}
print(f"player :{player}")

res = player.pop("age")
print(f"res :{res}")

res = player.pop("runs")
print(f"res :{res}")

print(f"player :{player}")
# res = player.pop()

print("popitem".center(60, "-"))
player = {'name': 'Rahul', 'age': 31, 'runs': 65, 'oppn': 'Pak', 'team': 'India', 'venue': 'Chepauk'}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")
print(f"player :{player}")