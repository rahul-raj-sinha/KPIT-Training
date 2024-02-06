
"""
Opening the file in read mode, if the file exists then opens the file for reading else will throw an exception - filenotfound error
"""

FL = open("data.txt",  "r")

# read - reads the entire contents of the file
# st = FL.read(1000)
# print(st)

# reads one line at a time
# st = FL.readline()
# print(st)

# st = FL.readline()
# print(st)
# print(len(st))

st = FL.readlines(860)
print(st)

# for line in st:
#     print(line)

FL.close()
