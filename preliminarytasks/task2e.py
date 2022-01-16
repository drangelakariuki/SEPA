# modify searchage() such that it gets the search age from the user.

def searchage():
    infile = open("names.txt", "r")
    age = int(input('Enter age you want to search with: '))
    for name in infile:
        name2 = name.split()
        if int(name2[1]) == age:
            print(name)
    infile.close()


searchage()
