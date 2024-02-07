

import re

st = "the @#$% ^&* quick brown fox jumps over the lazy dog"

res = re.search(r'\W+', st)

if res:
    print("Match found......")
    print(res.group(0))
else:
    print("Match not found.......")
