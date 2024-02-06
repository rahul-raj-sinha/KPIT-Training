
import re
# \d will match only numbers
# st = "my customer id is 23239234"
# res = re.search(r'\d+', st)

# \D - will match all non numeric data
st = "I dont remember the customer id number"

res = re.search(r'\D+', st)
if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found......")
