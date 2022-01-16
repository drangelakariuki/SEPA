# modify your program so that it first reads a letter from the user, and
# then prints only the lines where the name starts with that letter. Handle the lower/upper case issue.
# extra: Let the user search with a longer string. E.g. Search with Ah instead of A.

def searchname():
    infile = open("names.txt", "r")
    character = input('Enter character you want to search with: ')
    for name in infile:
        if name[0].upper() == character.upper():
            print(name)
    infile.close()


searchname()
