
from datetime import datetime

dt = datetime.now()
print(f"dt :{dt}")
print(type(dt))

print("-" * 60)
print("Day :", dt.strftime("%a"))
print("Day :", dt.strftime("%A"))

print("-" * 60)
print("Month :", dt.strftime("%b"))
print("Month :", dt.strftime("%B"))

print("-" * 60)
print("Year :", dt.strftime("%y"))
print("Year :", dt.strftime("%Y"))

print("-" * 60)
print("Date :", dt.strftime("%d"))
print("Date :", dt.strftime("%D"))
print("Date :", dt.strftime("%x"))

print("-" * 60)
print("Time :", dt.strftime("%T"))
print("Time :", dt.strftime("%X"))

print("-" * 60)
dt1 = dt.strftime("%d-%m-%y")
print(f"dt1 :{dt1}")

print("-" * 60)
dt2 = dt.strftime("%d-%m-%Y")
print(f"dt2 :{dt2}")
