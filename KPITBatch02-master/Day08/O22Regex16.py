

import re

st = "the@#$#$^234235345 quick brown fox jumps over the lazy dog"

res = re.search(r'\S+', st)

if res:
    print("Match found......")
    print(res.group(0))
else:
    print("Match not found.......")