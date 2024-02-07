
import re

st = "asTor tHe quick brown fox jumps over the lazy dog"

# res = re.search(r'\b(t\w+)', st, re.I)
res = re.search(r'\B(t\w+)', st, re.I)

if res:
    print("Match found......")
    print(res.group(0))
else:
    print("Match not found.......")