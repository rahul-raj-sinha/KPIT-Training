

import re

st = "the quick brown fox jumps over the lazy dog."

res = re.sub(r't\w+', "The", st, count = 1)

print(f"res :{res}")

print("-" * 60)
res = re.sub(r'fox', 'tiger', st)
# res = re.sub(r'(fox)', '\1.upper()', st)
print(f"res :{res}")
