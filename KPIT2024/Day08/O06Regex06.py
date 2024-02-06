
import re
# * - exactly n times of the character
# st = "baaat"
# res = re.search(r'ba{3}t', st)
#-------------------------------------------
# {n, } - n or more times
# st = "baaaaat"
# res = re.search(r'ba{3,}t', st)
st = "baaaaat"

res = re.search(r'ba{2,5}t', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found......")
