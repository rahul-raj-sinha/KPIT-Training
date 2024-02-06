
st = "hello world"
print(f"st :{st}")

print("-" * 60)
print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st10] :{st[10]}")

# Reverse Indexing
print("-" * 60)
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

#Slicing
print("-" * 60)
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[O:]   :{st[0:]}")
print(f"st[:11] :{st[:11]}")
print(f"st[:] :{st[:]}")

# slicing reverse
print("-" * 60)
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]  :{st[-1::-1]}")
print(f"st[:-12:-1] :{st[:-12:-1]}")
print(f"st[::-1]    :{st[::-1]}")

# write a code to check if the string is a palindrome
st = "malayalam"
res = "True" if st[0:9] == st[-1:-10:-1] else "False"
print(f"res:{res}")

print("-" * 60)
# maketrans and translate

st = "hello world"
print(f"st :{st}")
# length of a and b should be same
a = "helowrd"
b = "HELOWRD"

resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print(f"ord('h') :{ord('h')}")
print(f"ord('H') :{ord('H')}")
print(f"ord('e') :{ord('e')}")
print(f"ord('E') :{ord('E')}")

res = st.translate(resTbl)
print(f"res :{res}")
