# Day_03: Register Check

register = {"Michael": "yes", "John": "no", "Peter": "yes", "Mary": "yes"}


def register_check(new_dict: dict) -> tuple:
    """
        Checks the number of students in a school
        takes a dictionary as argument
        if student is in school,
         returns a tuple of 'yes' or 'no'  and number of students in school
    """
    name = input("\nEnter name to check if student is in school: \t").title()
    number_of_students = 0
    # the setdefault function searches for a given key in a dictionary and return the value if found
    # if key is not in the edictionary it returns a given set value which is usually set to "None"
    value = new_dict.setdefault(name, "no")
    for name in new_dict.values():
        if name == "yes":
            number_of_students = number_of_students + 1
    return (value, number_of_students)


print(register_check(register))


# Extra Challenge

name_list = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]


def name_lower(names: list) -> tuple:
    """
       takes a list of strings as argument
       checks for lowercase names
       returns an alphabetically sorted  tuple
    """
    new_list = []
    for name in names:
        if name == name.lower():
            new_list.append(name)
    # return a sorted tuple of names in lowercase
    return tuple(sorted(new_list))


print(f"{name_lower(name_list)}")
