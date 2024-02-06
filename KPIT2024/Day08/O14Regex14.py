
import re

st = """
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
"""

reg = re.compile(r't\w+')
print(f"reg :{reg}")
res = re.findall(reg, st)
print(res)
print(len(res), "\t", res.count("the"))

print('-' * 60)

res = re.search(reg, st)
if res:
    print(res.group(0))