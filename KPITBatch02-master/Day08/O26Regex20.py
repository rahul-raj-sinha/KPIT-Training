



import re

dt = "10-04-2014"

res = re.search(r'([0-2][1-9]|[1-3][0-1])(/|-)(0[1-9]|1[0-2])(\2)(19[0-9]{2}|2[0-9]{3})', dt)

if res:
    print("Match found......")
    print(res.group(0))
else:
    print("Match not found.......")