
import re

# st = "this is a sampLe Ample example"
st = "hello world"

print(f"st :{st}")

# res = re.search(r'\bample', st, re.I)
# res = re.search(r'\Bample', st, re.I)

# res = re.search(r'\Ahello', st)

res = re.search(r'world\Z', st)


if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found......")

