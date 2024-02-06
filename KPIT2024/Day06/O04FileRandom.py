
FL = open('data.txt', "rb")

pos = FL.seek(50, 0)
print(f"position :{pos}")

pos = FL.seek(100, 1)
print(f"position :{pos}")

pos = FL.seek(-75, 1)
print(f"position :{pos}")



FL.close()