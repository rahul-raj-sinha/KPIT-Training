



import re

st = "the quick brown fox jumps over the lazy dog"

res = re.search(r'fox', st)

if res:
    print("Match found......")
    print("rejected string :", st[:res.start()])
    print(res.group(0))
    print("unchecked string :", st[res.end():])
else:
    print("Match not found.......")