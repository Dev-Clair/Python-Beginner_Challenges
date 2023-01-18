# Day_29: Middle Figure

def middle_figure(str_1: str, str_2: str) -> str:
    """
       takes two string arguments
       joins them, finds and returns the middle element
       if no middle element, function returns no middle figure
    """
    new_str = (str_1 + " " + str_2).replace(" ", "")
    mid_val = len(new_str)
    if mid_val % 2 != 0:
        return new_str[mid_val//2]
    else:
        return f"\nno middle figure"


user_input_1 = input("\nEnter the first sentence: ")
user_input_2 = input("\nEnter the second sentence: ")
print(middle_figure(user_input_1, user_input_2))
