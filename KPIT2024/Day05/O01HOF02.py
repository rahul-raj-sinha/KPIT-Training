
def loginDetials(fnc):
    def bank_flow(amt):    # HOF
        print("-" * 60)
        print("Login")
        fnc(amt)
        print("logout")
        print("-" * 60)

    return bank_flow

@loginDetials
def withdraw(amt):
    print(f"debited {amt}.....")


@loginDetials
def deposit(amt):
    print("Credited.....")


# withdraw = loginDetials(withdraw)
withdraw(25000)             # calling bankflow
deposit(10000)


# write a decorator that calculates the time taken by a function to execute
