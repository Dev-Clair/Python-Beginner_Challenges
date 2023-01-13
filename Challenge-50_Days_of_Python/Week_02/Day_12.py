# Day_12: Count Dots

def count_dots():
    """
        Function called count_dots
        takes input from the user and returns the number of dots in USERINPUT
    """

    while True:
        print("\n\t\t\t ***************************\t\t\t")
        print("\t\t\t Welcome to Word_Dot Counter\t\t\t")
        print("\n\t\t\t ***************************\t\t\t")
        word = input(
            "\nGive me a word with each letter separated by dots and I'll count the dots in each word\n\t\t\t Enter \'q\' to quit \n\n\t\t\t Word: ")
        if word == 'q':
            break
        print(f"\nThe  number of dots in {word} is {word.count('.')}")


count_dots()
