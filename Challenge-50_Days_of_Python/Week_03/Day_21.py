# Day_21: List of Tuples

def make_tuples(lst_1, lst_2: list) -> list:
    """
       takes two lists as argument
       if they are equal, combines them and returns a list of tuples
       else returns an empty list
    """
    new_list = [(x, y)
                for x, y in zip(lst_1, lst_2) if len(lst_1) == len(lst_2)]
    return new_list


user_input1 = input(
    "\nEnter the elements of the first list separated by white spaces: \t").split()
user_input2 = input(
    "\nEnter the elements of the second list separated by white spaces: \t").split()
print(make_tuples(user_input1, user_input2))


# Extra Challenge

def even_or_average(*args) -> int:
    """
       reads user input up to specified limit
       returns the maximum even value in the list
       if no even value, it returns the average of the numbers 
    """
    # declare and initialize empty lists
    new_list = []
    even_list = []
    # with a while loop read input from user at runtime
    while True:
        user_input = int(input("\nEnter numbers: "))
        # if input is not divisible by 2, value is appended to the new_list list
        new_list.append(user_input)
        # if input is divisible by 2, value is appended to the even_list list
        if user_input % 2 == 0:
            even_list.append(user_input)
            # if condition breaks loop if userinput reaches the limit specified
        if len(new_list) == 5:
            break
    if len(even_list) > 0:
        # returns maximum value in the even_list sequence
        return max(even_list)
    else:
        # returns average value if no even entry was inputted by the user
        return sum(new_list)//len(new_list)


print(f"\n{even_or_average()}")
