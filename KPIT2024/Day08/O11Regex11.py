
import re

# st = "hello world"
# # \s searches for space
# res = re.search(r'\s', st)

st = "hello27329374@#@#$^&!world"

res = re.search(r'\S+', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found......")
