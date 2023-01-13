# Day_20: Capitlaize First Letter

def capitalize(str_inp: str) -> str:
    """
        takes a string argument as input
        capitalizes the first letter of each word
        returns value to caller
    """
    return str_inp.title()


user_input = input("\nEnter a sentence: ")
print((f"\n{capitalize(user_input)}"))


# Extra Challenge

str1 = 'leArning is hard, bUt if You appLy youRself ' \
    'you can achieVe success'


def reversed_list(str_inp: str) -> list:
    """
        takes a string of words as argument
        checks if each element contains a character in uppercase
        returns a reversed list of words containing uppercase characters only
    """
    # Declare and initialize an empty list
    emp_list = []
    # Convert string argument to list using the split function
    new_list = str_inp.split()
    # Use a for loop to iterate the list and
    for i in range(len(new_list)):
        # an inner for loop to iterate individual list -string- element
        for j in new_list[i]:
            if j == j.upper():  # if the character equals the character.upper()
                # append element to empty list
                emp_list.append(((new_list[i])[::-1]))
            else:
                continue
    return emp_list


print(reversed_list(str1))
