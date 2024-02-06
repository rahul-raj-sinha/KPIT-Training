

l = ['a', 'b', 'c', 'd', 'e']
print(F"l :{l}")

iterObj = iter(l)           # L.__iter__()

while True:
    try:
        elem = next(iterObj)
        print(f"elem , {elem}")
    except StopIteration:
        print("Exception Raised....")
        break
