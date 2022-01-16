# assignment 6, 3b
# a program that  prints only the lines
# where the name starts with the letter “A”


def searchname():
    infile = open("names.txt", "r")
    for name in infile:
        if name[0] == 'A':
            print(name)


searchname()
