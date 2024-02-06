
import re
# ^, $

st = "hello this is a good world"

print(f"st :{st}")

# check if the string is starting with hello
# r - raw string
res = re.search(r'^hello', st)

# end of the string
# res = re.search(r'world$', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found......")
