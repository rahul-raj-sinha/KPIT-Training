
FW = open("myfile.txt", "w")

# st = input("Enter contents for the file :")

# FW.write(st)
l1 = "This is the first line \n"
l2 = "This is the second line \n"
l3 = "This is the third line \n"

FW.writelines([l1, l2, l3])

FW.close()