

import re
st = "the quick brown fox jumps over the lazy dog."

res = re.sub('the', "The", st, 1)
print(f"res: {res}")



st1 = """
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick   brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
"""

for line in st1.splitlines():
    res = re.sub("the", "The", line, 1)
    print(res)