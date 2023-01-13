"""
    function called any_number
    can receive any number of arguments
    return the average of the input
"""


def any_number(*arg) -> float:
    """
        any_number is a function that takes variable number of arguments
        returns an integer values
    """
    average_value = sum(arg)/len(arg)
    return average_value


def main():
    # initialize an empty list
    counter = int(input("\nEnter the maximum number of elements: "))
    variadic = []
    # use a while loop to add values to the empty list
    while len(variadic) != counter:
        user_input = int(input("\nEnter the values to be added: \t"))
        variadic.append(user_input)
    # pass arguments to variadic function
    print(any_number(*variadic))


main()
