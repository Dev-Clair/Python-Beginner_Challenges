# Day_26: Sort Words

def sort_word(str_inp: str) -> list:
    """
        takes a string of words
        as an argument, removes the whitespaces and duplicate letters if any
        returns a list of letters sorted in alphabetical order.
    """
    new_str = ""
    for val in str_inp:
        if val not in new_str:
            new_str += val
    sorted(new_str)
    return list(new_str)


user_input = input("\nEnter a sentence: ")
print(sort_word(user_input))


# Extra Challenge

def string_length(str_input: str) -> dict:
    """
        takes a string of words as an argument
        returns length of words in a dictionary form.
    """
    # use the split function to convert the string to a list.
    new_list = str_input.split()
    # declare and initialize an empty dictionary
    new_dict = {}
    # use a for loop to iterate over the list and update the empty dictionary using the update method
    for word in new_list:
        new_dict.update({word: len(word)})
    return new_dict


user_input = input("\nEnter a sentence: ")
print(string_length(user_input))
