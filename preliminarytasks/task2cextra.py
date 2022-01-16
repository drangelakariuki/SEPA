# EXTRA: Let the user search with a longer string. E.g. Search with Ah instead of A.

def searchname():
    infile = open("names.txt","r")
    character = input('Enter characters you want to search with(the first two characters): ')
    for name in infile:
        if name[0:2].upper() == character.upper():
            print(name)
    infile.close()


searchname()