# Day_10: Hide Password

def hide_password():

    while True:
        import getpass
        password = getpass.getpass(
            "\nEnter password not longer than 4 characters: ")
        if len(password) > 4:
            password = password[0:4]
        print(f"\nYour password is 4 characters long:\t {password}\n")
        print("Will you like to try again? yes or no\n")
        check_again = input("\t\tchoice? ")
        if check_again == "no":
            break


hide_password()
