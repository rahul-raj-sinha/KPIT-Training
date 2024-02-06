import re

# st = "This is sample string"
# if (re.search(r"^This", st)):
#     print(True)
# else:
#     print(False)

# if (re.search(r"string$", st)):
#     print(True)
# else:
#     print(False)

# st = "bat bat"
# pattern = r"b.t"
# res = re.search(pattern, st)
# if res:
#     print(True)
#     print(res.group(0))
# else:
#     print(False)

# st = "bt"
# res = re.search(r'ba*t', st)    #True because a* means 0 occurance or more
# if res:
#     print(True)
# else:
#     print(False)

# st = "bat"
# # True because a? means 0 occurance or 1 occurance
# res = re.search(r'ba?t', st)
# if res:
#     print(True)
# else:
#     print(False)

# st = "bat"
# res = re.search(r'ba+t', st)    # True because a+ means 1 occurance or more
# if res:
#     print(True)
# else:
#     print(False)

# st = "baaat"
# res = re.search(r'ba{3}t', st)    # True because {n} means exact n numbers
# if res:
#     print(True)
# else:
#     print(False)

# st = "baaaaat"
# res = re.search(r'ba{3,}t', st)    # True because {n,} means atleast n numbers
# if res:
#     print(True)
# else:
#     print(False)

# st = "baaaaaaaat"
# res = re.search(r'ba{3,5}t', st)    # True because {n,m} means min n and max m
# if res:
#     print(True)
# else:
#     print(False)

# st = "bdh9t"
# res = re.search(r'b[a-zA-Z0-9]{3}t', st)
# if res:
#     print(True)
# else:
#     print(False)

# st = "boat"
# res = re.search(r'b(oa|a)t', st)
# if res:
#     print(True)
# else:
#     print(False)

# st = "LCNO-TEL-72-2010-0001"

# pattern = r"LCNO-(KAR|KER|APN|TND|TEL|MAH)-([0-6][1-9]|[1-7][0-3])-2[0-9]{3}-(?!0000)[0-9]{4}"
# pattern2 = r"LCNO-(KAR|KER|APN|TND|TEL|MAH)-([0-6][1-9]|[1-7][0-3])-2\d{3}-(?!0000)\d{4}"

# res = re.search(pattern, st)
# if res:
#     print("Valid Licensce")
#     print(res.group(0))
# else:
#     print("Invalid Licensce")

# st = "asTpr There tHe quick brown fox jumps over the lazy dog"
# # res = re.search(r"\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s", st)
# # res = re.findall(r"\b(t\w+)", st, re.I)
# # print(len(res))
# res = re.search(r"dog\Z", st)
# if res:
#     print(True)
#     print(res.group(0))
# else:
#     print(False)

# ptb2 = r"([0-2][1-9]|[1-3][0-1])(/|-)(0[1-9]|1[0-2])(\2)(19[0-9]{2}|2[0-9]{3})"
# st = "28/02/1923"
# # pattern = r"(\w+)\s(\w+)\s(\w+)\s(\2)"
# res = re.search(ptb2, st)
# if res:
#     print(True)
#     print(res.group(0))
# else:
#     print(False)

# st = "The quick brown fox jumps over the lazy dog fox"
# res = re.search(r"fox", st)

# print("Rejected string: ", st[:res.start()])
# print("Matched string: ", res.group(0))
# print("Unchecked String: ", st[res.end():])

# res2 = re.search(r"fox", st[res.end():])
# if res2:
#     print(True)
#     print(res2.group(0))
# else:
#     print(False)


# function:-
# findall
# finditer
# sub

# import re
# st = """
# the quick brown fox jumps over the lazy dog.
# the quick brown fox jumps over the lazy dog.
# the quick brown fox jumps over the lazy dog.
# the quick brown fox jumps over the lazy dog.
# the quick brown fox jumps over the lazy dog.
# the quick brown fox jumps over the lazy dog.
# the quick brown fox jumps over the lazy dog.
# the quick brown fox jumps over the lazy dog.
# the quick brown fox jumps over the lazy dog.
# the quick brown fox jumps over the lazy dog.
# the quick brown fox jumps over the lazy dog.
# the quick brown fox jumps over the lazy dog.
# """

# pattern = r"t\w+"
# # compile convert the string into a regex expression
# regex = re.compile(r"t\w+")
# res = re.findall(regex, st)
# print(f"res: {res}")
# print(len(res))

# res = re.finditer(r"t\w+", st)
# for i in res:
#     s = i.start()
#     e = i.end()
#     print(f"The string found between:{i.start()} and {i.end()} : {st[s:e]}")

# st = "the quick brown fox jumps over the lazy dog."
# res = re.sub(r"t\w+", "The", st, count=1)
# print(res)
# res = re.sub(r"fox", "tiger", st, count=1)
# print(f"res: {res}")

# st = "the quick brown fox jumps over the lazy dog."
# res = re.sub(r"fox", lambda word: word.upper(), st)
# print(res)
