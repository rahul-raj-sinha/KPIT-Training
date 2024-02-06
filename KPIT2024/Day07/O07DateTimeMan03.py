
import time
from datetime import datetime
import pytz

curtime = time.localtime()
print(curtime)
print("-" * 60)

curclock = time.strftime("%H : %M : %S", curtime)
print(curclock)
print("-" * 60)

# UTC - universal time coordinates
utc = pytz.utc
print(f"utc :{utc}")

print("-" * 60)
IST = pytz.timezone("Asia/Kolkata")
print(f"IST :{IST}")

print("-" * 60)
print(f"utc default format :{datetime.now(utc)}")

print("-" * 60)
IST = pytz.timezone("Asia/Kolkata")
NYT = pytz.timezone("America/New_York")
UKT = pytz.timezone("Europe/London")
AST = pytz.timezone("Australia/Melbourne")

print(f"IST :{datetime.now(IST)}")
print(f"NYT :{datetime.now(NYT)}")
print(f"UKT :{datetime.now(UKT)}")
print(f"AST :{datetime.now(AST)}")
