
from datetime import  datetime
import dateutils

dt1 = "Wednesday, September 13, 2021"
print(f"dt1 :{dt1}")
print(type(dt1))
print("-" * 60)

dt2 = "Friday, January 12, 2024"
print(f"dt2 :{dt2}")
print(type(dt2))
print("-" * 60)

actdt1 = datetime.strptime(dt1, "%A, %B %d, %Y")
print(f"actdt1 :{actdt1}")
print(type(actdt1))
print("-" * 60)

actdt2 = datetime.strptime(dt2, "%A, %B %d, %Y")
print(f"actdt2 :{actdt2}")
print(type(actdt2))
print("-" * 60)

print(f"actdt2 - actdt1 :{actdt2 - actdt1}")

print("-" * 60)
print("Difference in days :", dateutils.days(actdt2, actdt1))

print("-" * 60)
print("Difference in Months :", round(dateutils.months(actdt2, actdt1), 1))

print("-" * 60)
print("Difference in Years :", round(dateutils.years(actdt2, actdt1), 1))



