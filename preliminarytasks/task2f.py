# Add the main() function to your program. Your program should start from here.
# In this function, print the choices 1-search with name and 2-search with
# age as a menu and ask the user to choose one.
# Call the function searchname() or searchage() based on the number the user enters. If the user enters a
# number other than 1 or 2, print a warning message and end the program
def main():
    choice = int(input('Enter either 1 to search with name or 2 to search for age: '))
    if choice == 1:
        searchname()
    elif choice == 2:
        searchage()
    else:
        print('Error!Try Again')


def searchname():
    infile = open("names.txt", "r")
    character = input('Enter character you want to search with: ')
    for name in infile:
        if name[0].upper() == character.upper():
            print(name)
    infile.close()


def searchage():
    infile = open("names.txt", "r")
    age = int(input('Enter age you want to search with: '))
    for name in infile:
        name2 = name.split()
        if int(name2[1]) == age:
            print(name)
    infile.close()


main()
