
import re

st = "bbt"

# res = re.search(r'b[a-zA-Z0-9]t', st)
# res = re.search(r'b[aeiou]t', st)
res = re.search(r'b[^aeiou]t', st)

if res:
    print("Match found......")
    print(res.group(0))
else:
    print("Match not found.......")