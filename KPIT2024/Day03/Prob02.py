
st = "abcd"

for i in range(0, len(st)):
    for j in range(i, len(st)+1):
        if st[i:j] == "":
            continue
        else:
            print(st[i:j], end=" ")

