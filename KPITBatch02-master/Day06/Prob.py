
ch = "yes"
s = ""
while(ch == "yes"):
    st = input("Enter the contents of the file :")
    s += st+"\n"
    ch = input("Do you want to continue :")

FW = open("myfile1.txt", "w")
FW.write(s)
FW.close()
