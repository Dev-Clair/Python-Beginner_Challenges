# Day_27: Unique Numbers

def unique_numbers(lst_1: list) -> list:
    """
       takes a list argument
       returns the difference between the lists if there is a unique number
       else the original list if no unique number
    """
    lst_2 = [int(val) for val in lst_1]
    lst_3 = []
    for num in lst_2:
        if num not in lst_3:
            lst_3.append(num)
    list_diff = sum(lst_2) - sum(lst_3)
    if list_diff % 2 == 0:
        return lst_2
    else:
        return lst_3
    # return list_diff


user_input = input(
    "\nEnter integer or float values separated by whitespaces: ").split()
print(unique_numbers(user_input))


# Extra Challenge

def difference(lst_1: list, lst_2: list) -> list:
    """
       takes two lists as argument
       returns a list of that contains elements in the first list which is not in the second and vice versa
    """
    lst_3 = [int(val_1) for val_1 in lst_1 if val_1 not in lst_2]
    lst_4 = [int(val_2) for val_2 in lst_2 if val_2 not in lst_1]
    final_lst = lst_3 + lst_4
    return final_lst


user_input_1 = input(
    "\nEnter integer or float values separated by whitespaces: ").split()
user_input_2 = input(
    "\nEnter integer or float values separated by whitespaces: ").split()
print(difference(user_input_1, user_input_2))
