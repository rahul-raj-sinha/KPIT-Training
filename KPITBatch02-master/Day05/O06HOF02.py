
def bankJob(fnc):
    print("logging into the server")
    fnc()
    print("logging out of the server")
    print("-" * 60)

def deposit():
    print("Amount credited into the account.....")

def withdraw():
    print("Amount debited from the account.....")


bankJob(deposit)
bankJob(withdraw)