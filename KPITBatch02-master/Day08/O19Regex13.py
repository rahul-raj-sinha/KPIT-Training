

import re

st = "the quick brown 345345345 fox jumps over the lazy dog"

res = re.search(r'\d+', st)

if res:
    print("Match found......")
    print(res.group(0))
else:
    print("Match not found.......")