

def bankJob(fnc):
    def helper(amount):
        print("logging into the server")
        fnc(amount)
        print("logging out of the server")
        print("-" * 60)

    return helper

@bankJob
def deposit(amt):
    print(f"Amount {amt} credited into the account.....")

@bankJob
def withdraw(amt):
    print(f"Amount {amt} debited from the account.....")







