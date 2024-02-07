
glbX = 100

def fun(i):         # i is a local variable
    global glbX         # do not assign any value in this line
    print(f"i :{i}")
    j = 50          # j is a local variable
    print(f"j :{j}")
    glbX += 500
    print(f"glbX inside :{glbX}")

print(f"before :{glbX}")

fun(50)

print(f"after :{glbX}")

