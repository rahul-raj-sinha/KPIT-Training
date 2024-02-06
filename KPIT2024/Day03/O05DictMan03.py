
# pop
player = {'name': 'Rahul', 'age': 36, 'runs': 120, 'oppn': "Aus"}
print(f"player :{player}")

res = player.pop('runs')
print(f"res :{res}")
print(f"player :{player}")

res = player.pop('oppn')
print(f"res :{res}")
print(f"player :{player}")

print("-" * 60)
# popitem
player = {'name': 'Rahul', 'age': 36, 'runs': 120, 'oppn': "Aus"}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")
print(f"player :{player}")

print("-" * 60)
# items = combination of keys and values functions

emp = {'emp1': {'name': 'Kevin', 'age': 32, 'desig': 'Team Lead', 'dept': 'MKT', 'sal': 65000},
       'emp2': {'name': 'Kenith', 'age': 45, 'desig': 'MGR', 'dept': 'Finance', 'sal': 85000},
       'emp3': {'name': 'Richard', 'age': 39, 'desig': 'PM', 'dept': 'IT', 'sal': 265000}
       }

print(f"emp :{emp}")

print("-" * 60)

print(f"Emp1 :{emp['emp1']}")

print("-" * 60)
print(f"Emp2 :{emp['emp2']}")

print("-" * 60)
print(f"Emp3 :{emp['emp3']}")

print("-" * 60)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k + " => " + str(v))
    print("-" * 60)

print("-" * 60)

emp1 = {'name': 'Kevin', 'age': 32, 'desig': 'Team Lead', 'sal': 65000}
emp2 = {'name': 'Kenith', 'age': 45, 'desig': 'MGR', 'dept': 'Finance'}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

emp1.update(emp2)
print("-" * 60)
print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 60)

emp1 = {'name': 'Kevin', 'age': 32, 'desig': 'Team Lead', 'dept': 'MKT', 'sal': 65000}
print(f"emp1 :{emp1}")

emp1.clear()
print(f"emp1 :{emp1}")
