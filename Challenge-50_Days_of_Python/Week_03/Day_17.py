"""
    function called user_name
    creates a User Name for User
"""


def user_name():
    from random import randint
    """
    Asks user to input name of choice
    reverses the name and attach a random number between 0 and 9
    returns username
    """
    # use a while loop to repeat process until user is satisfied with username generated
    while True:
        print("\nWelcome to User Name Generator")
        # read values from standard input
        name = input("\nEnter a name of your choice: \t").capitalize()
        # perform string reversal and concatenantion oppening
        result = (name[::-1]) + str(randint(0, 9))
        # print output to sttandard output
        print(f"\nyour username is {result}")
        # ask user to try-again if they aren't satisfied with result
        print("\nWill you like to try-again? yes or no")
        choice = input("\nChoice: \t")
        if choice == "no":
            break


user_name()
