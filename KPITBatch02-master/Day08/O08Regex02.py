
import re

st = "bait"

res = re.search(r'b..t', st)

if res:
    print("Match found......")
    print(res.group(0))         # string that matched the regex
else:
    print("Match not found")

