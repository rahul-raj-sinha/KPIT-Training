
def outerFun():
    gname = "Rahul"
    def innerFun():
        nonlocal  gname

        gname  = "Mr." + gname
        print("Hello World")
        print(f"Greetings {gname}")

    innerFun()
    print(f"After :{gname}")

outerFun()
