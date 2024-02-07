
FL = open("data.txt", "rb")

pos = FL.seek(50, 0)
print(f"pos :{pos}")

pos = FL.seek(100, 1)
print(f"pos :{pos}")

pos = FL.seek(-45, 1)
print(f"pos :{pos}")

pos = FL.seek(0, 2)
print(f"pos :{pos}")

pos = FL.seek(-10, 0)

FL.close()