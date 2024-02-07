
import re

st = "the233464786978 quick brown fox jumps over the lazy dog"

res = re.search(r'\w+', st)

if res:
    print("Match found......")
    print(res.group(0))
else:
    print("Match not found.......")