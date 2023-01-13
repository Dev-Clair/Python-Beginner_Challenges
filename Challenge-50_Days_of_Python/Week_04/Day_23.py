# Day_23: Simple Calculator

def choice(opt: int):
    match opt:
        case 1:
            print(f"\n\t The answer is: {add()}")
        case 2:
            print(f"\n\t The answer is: {subtract()}")
        case 3:
            print(f"\n\t The answer is: {multiply()}")
        case 4:
            print(f"\n\t The answer is: {divide()}")
        case _:
            print(catch_all())


def add():
    """
        takes input from user and returns result
    """
    print("\n\tYou have selected Addition")
    val_01 = float(input("\nEnter First Value: "))
    val_02 = float(input("\nEnter Second Value: "))
    try:
        result = val_01 + val_02
    except ValueError:
        print("\nWrong entry.\nPlease Try Again")
    else:
        return result


def subtract():
    """
        takes input from user and returns result
    """
    val_01 = float(input("\nEnter First Value: "))
    val_02 = float(input("\nEnter Second Value: "))
    print("\n\tYou have selected Subtraction")
    try:
        result = val_01 - val_02
    except ValueError:
        print("\nWrong entry.\nPlease Try Again")
    else:
        return result


def multiply():
    """
        takes input from user and returns result
    """
    val_01 = float(input("\nEnter First Value: "))
    val_02 = float(input("\nEnter Second Value: "))
    try:
        result = val_01 * val_02
    except ValueError:
        print("\nWrong entry.\nPlease Try Again")
    else:
        return result


def divide():
    """
        takes input from user and returns result
    """
    print("\n\tYou have selected Division")
    val_01 = float(input("\nEnter First Value: "))
    val_02 = float(input("\nEnter Second Value: "))
    try:
        result = val_01 / val_02
    except ZeroDivisionError:
        print("\nDivisor cannot be zero.\nPlease Try-Again")
        val_02 = float(input("\nEnter Second Value: "))
        result = val_01 / val_02
    return result


def catch_all():
    if NameError | ValueError:
        return f"\nNot a valid entry"


def main():
    """
        A simple calculator that perform basic math operations
    """
    while True:
        print("\n\t\t\tSimple Calculator")
        print("\nSelect the option that corresponds to the operation you want to carry out")
        print("1. Addition\t 2. Subtraction\n3. Multiplication\t4. Division")
        choice(int(input("\nChoice: ")))
        retry = input("\nDo you want to try again ? ")
        if retry == "no":
            break


main()


# Extra Challenge

def append_list(a: str, b: int) -> str:
    """
        takes a string and integer as argument
        returns a formatted output
    """
    return "{}({})".format(a, b)


def lst_str(c: list) -> str:
    """
        takes a list as argument and
        returns a formatted output of strings
    """
    str2 = ", "
    return str2.join(map(str, c))


def multiply_words(str1: str):
    """
        takes a string as an argument
        multiplies the length of each word in the string by the length of other words in the string
        function should only multiply words with all lowercase letters
    """
    words_list = str1.split()
    words_length = []
    str2 = ","
    total_length = 1
    for word in words_list:
        if word.islower():
            total_length = total_length * len(word)
            # appends a list with arguments supplied by the the append_list function
            words_length.append(append_list(word, len(word)))

    #  alternatively, str2.join(map(str, words_length)) can be used to return a formatted list of the words and their length
    return f"\n{total_length}: {lst_str(words_length)}\n"


user_input = input("\nEnter a sentence: ")
print(multiply_words(user_input))
