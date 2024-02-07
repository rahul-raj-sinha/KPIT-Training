
st = 'hello world'
print(f"st :{st}")

a = "helowrd"
b = "HELOWRD"

# length of a and b should be same

resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

res = st.translate(resTbl)
print(f"res :{res}")
