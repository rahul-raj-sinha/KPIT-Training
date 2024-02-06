
def get_name(surname):
    print(f"surname is {surname}")

    while (True):
        name = yield                # accepting data
        print(f"Name recieved is :{name}")
        print("-" * 60)
        if surname in name:
            print(f"surname {surname} found in {name}")

coObj = get_name("Pillai")

print(coObj)
coObj.__next__()
coObj.send("Sachin Tendulkar")
coObj.send('Rahul Dravid')
coObj.send("Yuraj Singh")
coObj.send("Dhanraj Pillai")
