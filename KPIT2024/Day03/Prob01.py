
def CreateMatrix(st):
    print(st + " Matrix")
    rc = st.split("x")
    # print(int(rc[0]))

    mat = []
    for i in range(0, int(rc[0])):
        r = []
        for j in  int((rc[1])):
            r.append(0)
        mat.append(r)
    return mat


st = input("Enter the matrix dimension :")
mat = CreateMatrix(st)
print(mat)
