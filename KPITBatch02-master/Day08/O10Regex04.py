
import re

st = "bat"

res = re.search(r'ba?t', st)

if res:
    print("Match found......")
    print(res.group(0))
else:
    print("Match not found.......")