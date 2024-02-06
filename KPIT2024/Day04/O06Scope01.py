
glbX = 100

def fun(y):     # y is a local var
    global glbX

    print(f"y :{y}")
    glbX = 250
    print(f"glbx inside :{glbX}")



print(f"glbx before :{glbX}")

fun(500)

print(f"glbx after :{glbX}")