
# FW = open("sample.txt", "w")
#
# ch = "y"
# lines = ""
#
# while (ch == "y"):
#     line = input("enter the contents of the file :")
#     lines += line + "\n"
#
#     ch = input("Do you want to continue :")
#
# FW.write(lines)
# FW.close()


print("-" * 60)

FW = open("sample1.txt", "w")

ch = "y"
lines = []

while (ch == "y"):
    line = input("enter the contents of the file :")
    lines.append(line + "\n")

    ch = input("Do you want to continue :")

for i in range(len(lines)-1, -1, -1):
    FW.write(lines[i])

FW.close()
