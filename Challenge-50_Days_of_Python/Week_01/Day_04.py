# Day_04: Only Float

def main():
    a = float(input("\nEnter the first number: \t"))
    b = float(input("\nEnter the second number: \t"))
    result = only_float(a, b)
    print(result)


def only_float(value01, value02):
    """
        takes two arguments - a and b
        returns 2 if both arguments are floats
        returns 1 if only one argument is a float
        returns 0 if none of the arguments are floats
    """
    if type(value01) == float and type(value02) == float:
        return 2
    elif type(value01) == float or type(value02) == float:
        return 1
    else:
        return 0


main()

# Extra Challenge

furnitures = ['Mattress', 'Pillows', 'Sheets', 'Hisense Sound Bar', 'Cooker', 'Chairs',
              'Otto-stools', 'Curtains', 'Pots', 'Television', 'Play-station']


def word_index(item_list: list):
    """
        A function that takes one argument - a list of strings
        returns the index of the longest word
    """
    # To return the longest word in the list
    # return max(item_list, key=lambda x: len(x))

    # To return the index of the longest word in the list
    return max(enumerate(item_list), key=lambda x: len(x[1]))[0]


print(
    f"The longest word has the index position: {word_index(furnitures)}")
