# Day_24: Average Calories

def average_calories():
    """
        calculates the average calorie intake of a user.
    """
    total_calories = 0  # initialize total calories consumed
    count = 0  # initialize counter variable
    days_value = int(
        input("\nEnter the number of days you had a calorie diet: "))
    while count != days_value:
        calorie_value = int(
            input("\nEnter your calorie intake for each day: "))
        total_calories += calorie_value
        count += 1
    result = total_calories/days_value
    return f"\nYour average calorie intake over {days_value}-days is {result:2f}\n"


print(average_calories())


# Extra Challenge

def nested_lists() -> list:
    """
        takes any nummber of lists
        returns a nested list
    """
    count = 0  # initialize counter variable
    nest_list = []  # initialize an empty list
    list_num = int(
        input("\nEnter the number of sub-lists you want to create: "))
    while count != list_num:
        new_list = input("\nEnter Values: ").split(sep=",",
                                                   maxsplit=list_num)  # reads entries from standard input
        nest_list.append(new_list)  # appends sub-list to list
        count += 1  # increments per loop
    return nest_list


print(nested_lists())
