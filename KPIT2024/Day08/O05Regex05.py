
import re
# * - one or more occurances of the character
st = "bat"
# st = "baaaaaaaaaaaaaaaaaaaaaaaaaat"

res = re.search(r'ba+t', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found......")
