
def outerFun(inf):      # HOF - Higher Order Function
    inf = "Mr." + inf
    def innerFun():

        print(f"Hello {inf}")

    return innerFun

refInr = outerFun("Sachin")


# we lost the scope of the variables  outerfun
refInr()

print("-" * 60)

outerFun("Rahul")()     # calls the innerfun
