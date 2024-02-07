
emp = {
    'emp1': {'empid': 101, 'empname': 'Mike', 'age': 27, 'dept':'MKT', 'desig': 'BDE'},
    'emp2': {'empid': 102, 'empname': 'Tina', 'age': 25, 'dept':'Finance', 'desig': 'FE'},
    'emp3': {'empid': 103, 'empname': 'Kevin', 'age': 34, 'dept':'IT', 'desig': 'PL'}
}

print(f"emp :{emp}")
print("-" * 60)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

# items = keys + values
print("-" * 60)

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>",  v)

    print("-" * 40)

print("update".center(60, "-"))
emp1 = {'empid': 101, 'empname': 'Mike', 'age': 27,  'desig': 'BDE'}

print(f"emp1 :{emp1}")

emp2 = {'empid': 102, 'empname': 'Tina', 'age': 25, 'dept':'Finance'}

print(f"emp2 :{emp2}")

emp1.update(emp2)
print(f"emp1 :{emp1}")




