
def outerFun():
    gname = "Rahul"         # local variable
    def innerFun():
        nonlocal  gname     # only local variables can be converted as nonlocal variables
        gname = "Mr." + gname
        print(f"Greetings {gname}")
        print("Hello World")

    innerFun()

outerFun()