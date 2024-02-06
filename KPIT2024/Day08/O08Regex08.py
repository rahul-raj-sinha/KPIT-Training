

import re
# * - zero or more occurances of the character

st = "bout"

res = re.search(r'b(ai|ou)t', st)
   
if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found......")
