"""
    functions called count_words and count_elements
    count_words return number of words
    count_element returns number of elements without counting whitespaces
"""


def main():
    # use a while loop to repeat process until user is satisfied with output
    while True:
        user_input = input(
            "\n Type in  a sentence and I'll count the number of words and elements in it:\n\t").capitalize()
        print(
            f"\n'{user_input}' contains {count_words(user_input)} words and {count_elements(user_input)} characters")
        print("\nWill you like to try again? Yes or no")
        try_again = input("\nChoice:\t")
        if try_again == "no":
            break


def count_words(userinput: str) -> int:
    # returns number of elements is string list
    return len(userinput.split())


def count_elements(userinput: str) -> int:
    # returns integer value subtracted from lenth of string with whitespace
    return (len(userinput) - int(userinput.count(" ")))


if __name__ == "__main__":
    main()
