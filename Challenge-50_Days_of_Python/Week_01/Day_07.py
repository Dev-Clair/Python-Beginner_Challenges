# Day_07: String Range


def string_range():
    """
        reads input from user
        returns a a range of numbers separated by dot
    """
    while True:
        usr_inpt = int(input("\nEnter an Integer Value: \t"))
        for element in range(usr_inpt):
            print(element, end=".")
        print("\nWill you like to enter another number? 'yes' or 'no'")
        try_another = input("\nChoice: ")
        if try_another == "no":
            break


string_range()


#  Extra Challenge

names = ["Joseph", "Nathan", "Sasha", "Kelly",
         "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]


def list_to_dict(names: list) -> dict:
    """
        A function that takes one argument - a list of names
        returns a dictionary of the names that start with "S" as keys
    """

    dict_names = {}
    for name in names:
        if name.startswith("S"):
            dict_names.update({name: names.count(name)})
    return dict_names


print(list_to_dict(names))
