# Day_05: My Discount

def my_discount():
    """
        Function called my_discount
        Asks for USERINPUTS - price and discount
        Calculates and returns price after discount
    """
    print("\nDo you want to check the price of an item? yes or no\n")
    item_price = input("\tChoice? ").lower()
    while item_price != "no":
        try:
            price = float(input("\nPlease Enter the Item's Price: \t"))
            discount = float(input("\nPlease Enter Discount on label: \t"))/100
            return (price - price*discount)
        except ValueError:
            print("\n\tOne of the entries is incorrect.\n\tPlease Enter Again Correctly")


print(f"\nThe price for the item is {my_discount()} Naira")


# Extra Challenge

students = ['Male', 'Female', 'Female', 'Male', 'Male', 'Male',
            'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']


def tuple_of_sex(n: list) -> list:
    """
        A function that takes one argument - a list of strings
        returns a formatted list of tuple
    """

    j = n.count('Male')
    k = n.count('Female')
    Male = ('Male', j)
    Female = ('Female', k)
    Sex = [Male, Female]
    return Sex


print(tuple_of_sex(students))
