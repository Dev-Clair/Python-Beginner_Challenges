# Day_08: Odd Even

list_num = [3, 41, 2, 12, 17, 25, 16, 19]


def odd_even(list_var: list) -> int:
    """
        takes a list of numbers as argument
        returns difference between largest even number and smallest odd number
    """
    # initialize list variables with empty lists
    n_even = []
    n_odd = []
    for num in list_var:
        if num % 2 == 0:
            n_even.append(num)  # appends even numbers to empty list
        else:
            n_odd.append(num)  # appends odd numbers to empty list
    # max and min functions return maximun and minimum values of arguments
    result = (max(n_even) - min(n_odd))
    return result


# list_num = input("\nEnter the odd and even values in any order and i'll return the difference between the maximum even and minimum odd values\nEnsure the values are separated by a comma:\t").split()
print(odd_even(list_num))
