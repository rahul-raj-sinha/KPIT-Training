
import re
# \w - mathces alpha numeric characters
# st = "this2343 45234 is a sample text"
# print(f'st :{st}')

st = "@#$% ^&*! hello world"

res = re.search(r'\W+', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found......")
