
import re

dt = "31-03-2021"

res = re.search(r'([0-2][1-9]|[1-3][0-1])(/|-)((!?29, 0[1-9]|1[0-2])(\2)(19[0-9]{2}|[2-9][0-9]{3})', dt)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found......")

