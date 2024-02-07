
# match, search, findall, finditer, compile, sub,

import re

st = "this is a sample string"
print(f"st :{st}")

if re.match(r"^this", st):
    print("Match found \n")
else:
    print("Match not found.")

if re.search(r"string$", st):
    print("Match found \n")
else:
    print("Match not found.")