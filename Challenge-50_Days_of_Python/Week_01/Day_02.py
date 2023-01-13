# Day_02: Convert Add

list_string = ['4', '8', '12', '16', '20', '24', '28']


def convert_add(lst_strng: list):
    """
        function called convert_add
        takes a list as argument
        converts string to integers and sums the list
        returns value back to caller
    """
    new_list = list(map(int, lst_strng))
    return sum(new_list)


print(convert_add(list_string))


# Extra Challenge

list_string = ["Rotimi", "Emeka", "Leye", "Tupac", "Samuel", "Sunday",
               "Joshua", "Emmanuel", "Andrew", "Destiny", "Agogo", "Samuel"]


def check_duplicate(new_list: list):
    """
        checks if there are duplicates
        returns duplicate if any
        else function returns "No Duplicates"
    """

    for value in range(0, len(new_list)):
        for check in range(1, len(new_list)):
            if value == check:
                return value
    else:
        return f"No Duplicates"


print(f"\n{check_duplicate(list_string)}")
