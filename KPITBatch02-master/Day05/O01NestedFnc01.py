
def outerFun():         # HOF Higher Order Function
    gname = "Sachin"
    def InnerFun():

        print('Hello World')
        print(f"Greetings Mr.{gname}")

    return InnerFun

Inref = outerFun()
Inref()

print("-" * 60)

outerFun()()            # calls the innerFun



