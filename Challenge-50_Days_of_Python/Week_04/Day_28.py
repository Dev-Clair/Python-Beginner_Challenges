# Day_28: Index Position

def index_position(str_1: str) -> list:
    """
       takes a string argument
       returns the index of all lowercase letters in the string
    """
    ind_pos = []
    for let in str_1:
        if let.islower():
            ind_pos.append(str_1.index(let))
    return ind_pos


user_input = input("\nEnter a string of lower and upper case letters: ")
print(index_position(user_input))


# Extra Challenge

def largest_number(str_2: list) -> str:
    """
       takes a list argument
       returns the maximum number possible formatted by a thousand separator
    """
    new_str = "".join(sorted(str_2, reverse=True))
    return "{:,}".format(new_str)


user_input = input("\nEnter integer values separated by whitespaces: ").split()
print(largest_number(user_input))
