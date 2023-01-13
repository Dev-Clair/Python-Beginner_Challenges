# Day_25: All The  Same

def all_the_same(arg: list) -> bool:
    """
        takes one argument - a list, string or tuple
        returns True if the elements are the same else False
    """
    # if type(arg) == list or type(arg) == tuple or type(arg) == str:
    for element in arg:
        if element == element[:1]:
            return True
        else:
            return False


user_input = input("\nEnter values: ").split()
print(all_the_same(user_input))


# # Extra Challenge


# def read_backwards(arg: list) -> str:
#     """
#         takes a list as argument and
#         returns a formatted output of strings
#     """
#     arg.reverse()
#     return " ".join(arg)


# user_input = input("\nEnter a sentence: ").split()
# print(read_backwards(user_input))
