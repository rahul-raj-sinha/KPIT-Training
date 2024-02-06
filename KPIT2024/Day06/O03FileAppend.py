"""
append mode - if the file already exists then append the new contents without disturbing the previous data. if the file does not exist then creates a new file and adds the contents into it
"""

FA = open("myfile.txt", "a")

st = input("Enter the contents of the file :")

FA.write(st + "\n")

FA.close()