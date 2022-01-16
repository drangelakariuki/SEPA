# Define a new function named searchage().#
# Again, copy the code that opens and prints the file.
# This time, modify the code such that it prints only the lines where the age is equal to 5.

def searchage():
    infile = open("names.txt", "r")
    for name in infile:
        name2 = name.split()
        if int(name2[1]) == 5:
            print(name)
    infile.close()


searchage()
