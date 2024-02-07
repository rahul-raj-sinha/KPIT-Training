

FL = open("C:\\Training\\PycharmProjects\\KPITBatch02\\Day06\\data.txt", "r")

# st = FL.read(100)           # will read the entire contents of the file

# st = FL.readline()          # can read one line
# print(st)

# st = FL.readlines()
# print(st)

for st in FL.readlines(900):
    print(st)

FL.close()