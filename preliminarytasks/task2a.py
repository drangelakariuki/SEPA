# this function prints the line(names) in the file including \n which prints a new
# line in a text file.
def searchname():
    infile = open("names.txt", "r")
    for s in infile:
        print(s)


searchname()


# this function prints the names in the file without the \n, because of the string indexing
# [-1] which prints the names 'backwards ' without the character \n which prints a new line

def searchname():
    infile = open("names.txt", "r")
    for s in infile:
        print(s[:-1])


searchname()
