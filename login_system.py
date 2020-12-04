users = {}
status = ""


def displaymenu():
    status = input("Are you registered user? y/n? press q to quit")
    if status == "y":
        olduser()
    elif status == "n":
        newuser()


def newuser():
    createlogin = input("create login name: ")

    if createlogin in users:
        print("\nlogin name already exists!\n")
    else:
        createpassw = input("create password: ")
        users[createlogin] = createpassw
        print("\nuser created\n")


def olduser():
    login = input("enter login name: ")
    passw = input("enter password: ")

    if login in users and users[login] == passw:
        print("\nlogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")


while status != "q":
    displaymenu()
