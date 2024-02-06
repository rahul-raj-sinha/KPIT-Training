

import re
# [] - character class

# st = "but"
# res = re.search(r'b[aeiou]t', st)

# -------------------------------------

# st = "bzt"
# res = re.search(r'b[^aeiou]t', st)

# --------------------------------------
st = "bAt"
res = re.search(r'b[a-z0-9A-Z]t', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found......")
