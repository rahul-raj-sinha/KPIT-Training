
# copy
emp1 = {'name': 'Kevin', 'age': 32, 'desig': 'Team Lead', 'sal': 65000}
print(f"emp1 before :{emp1}")

# copy from dictionary emp1 to emp2
emp2 = emp1         # shallow copy - copies the data with the address

print(f"emp2 before :{emp2}")

emp2['dept'] = "MKT"
emp2['gender'] = "Male"

print()
print("-" * 60)

print(f"emp1 after :{emp1}")
print(f"emp2 after :{emp2}")

print("copy".center(40, "="))
emp3 = {'name': 'Kevin', 'age': 32, 'desig': 'Team Lead', 'sal': 65000}
print (f"emp3 before :{emp3}")

emp4 = emp3.copy()
print(f"emp4  before:{emp4}")

emp4['dept'] = "Finance"
emp4['loc'] = "Mumbai"

print(f"emp3 after :{emp3}")
print(f"emp4 after :{emp4}")

print("-" * 60)
emp5 = {'name': 'Kevin', 'age': 32, 'desig': 'Team Lead','experience': {'HP':3, 'IBM':2, 'Wipro': 5},'sal': 65000}

print(F"emp5 :{emp5}")

emp6= emp5.copy()

emp6['experience']['amazon'] = 4
emp6['experience']['dell'] = 1

print(f"emp5 after :{emp5}")
print(f"emp6 after :{emp6}")

print("-" * 60)
from copy import deepcopy
emp7 = {'name': 'Kevin', 'age': 32, 'desig': 'Team Lead','experience': {'HP':3, 'IBM':2, 'Wipro': 5},'sal': 65000}
print(f"emp7 :{emp7}")

emp8 = deepcopy(emp7)
print(f"emp8 before :{emp8}")

emp8['experience']['amazon'] = 4
emp8['experience']['dell'] = 1
print()
print("-" * 60)
print(f"emp7 after :{emp7}")
print(f"emp8 after :{emp8}")

# https://pythontutor.com/render.html#mode=display