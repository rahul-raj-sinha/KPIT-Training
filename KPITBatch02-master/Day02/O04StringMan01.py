
st = "hello world"
print(f"st :{st}")
print(type(st))

print("-" * 60)
print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 60)
#reverse indexing
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 60)
# slicing
print(f"st[0:5:1] : {st[0:5:1]}")
print(f"st[6:11]  :{st[6:11]}")
print(f"st[0:11]  :{st[0:11]}")
print(f"st[0:]    :{st[0:]}")
print(f"st[:11]   :{st[:11]}")
print(f"st[:]     :{st}")

print("-" * 60)
# slicing in reverse
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-6:-12:-1] :{st[-6:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[::-1]      :{st[::-1]}")

# stirngs are immutable

st = "hello world"
print(f"st :{st}")

# print(f"st[0] :{st[0]}")
# st[0] = "H"

print("find".center(60, "-"))

st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print(f"st1 :{st1}")
idx = st1.find("l")               # returns the index
print(f"index :{idx}")

idx = st1.find("l", st1.find("l", st1.find("l") + 1) + 1)
print(f"index :{idx}")

print("-" * 60)
print(f"st2 :{st2}")

idx = st2.find("fox")
print(f"index :{idx}")

print("replace".center(60, "-"))
print(f"st1 :{st1}")
res = st1.replace("h", "H")
print(f"res :{res}")

res = st1.replace("l", "L")
print(f"res :{res}")

res = st1.replace("l", "L", 1)
print(f"res :{res}")

res = st1.replace("l", "L", 2)
print(f"res :{res}")

print("-" * 60)
print(f"st2 :{st2}")

res = st2.replace("fox", "tiger")
print(f"res :{res}")

res = st2.replace("the", "The")
print(f"res :{res}")

res = st2.replace("the", "The", 1)
print(f"res :{res}")

print("-" * 60)
print(dir(st1))
