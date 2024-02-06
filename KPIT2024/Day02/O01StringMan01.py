
st = "hello world"
print(f"st: {st}")
print(type(st))

# print(dir(st))

print("-" * 60)
print(f"st :{st}")

print(f"st[0] :{st[0]}")
# str[0] = "H"

st = "HELLO WORLD"

print("-" * 60)
st =  "hello world"
st1 = "the quick brown fox jumps over the lazy dog"

print(f"st :{st}")
print(f"st1 :{st1}")

print("find".center(60, "-"))

res = st.find("w")
print(f"res :{res}")

res = st1.find("fox")
print(f"res :{res}")

print("-" * 60)

print("replace".center(60, "-"))
print(f"st :{st}")
res = st.replace("l", "L", 2)
print(f"res :{res}")

r = st[6:].replace("l", "L")
print(f"r :{r}")

print(f"st1 :{st1}")
res = st1.replace("fox", "tiger")
print(f"res :{res}")

print("index".center(60, "-"))
res = st.index("w")
print(f"res :{res}")

res = st.index("l")
print(f"res :{res}")

res = st.index("l", 3, 5)
print(f"res :{res}")

res = st.index("l", 5)
print(f"res :{res}")

print(f"st1 :{st1}")
res = st1.find("fox")
print(f"res :{res}")

res = st1.find("the")
print(f"res :{res}")

res = st1.find("the", 3)
print(f"res :{res}")
