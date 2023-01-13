# Day_09: Biggest Odd


def biggest_odd():
    """
        takes a string of numbers as argument
        returns the biggest odd number in the list
    """
    value = input(
        "\nEnter a string of integer numbers (Hint: without whitespaces): ")
    # use list comprehension to iterare through the string and append result to the list variable num_odd
    num_odd = [val for val in value if int(val) % 2 != 0]
    return max(num_odd)


print(biggest_odd())


# Extra Challenge

# def zeros_last(value: list) -> list:
#     """
#         takes an argument - a list of input from the user
#         if the list contains zeros, it moves them to the end of the list
#         while maintaining the order of the other elements
#         else, if there are no zeros, it returns a sorted list in ascending order
#     """
#     result = [x for x in value if x != 0]
#     for num in value:
#         if num not in result:
#             result.append(num)
#     return result


# list_num = input(
#     "\nEnter the values of the list separated by white spaces: \t").split()
# print(f"\n{zeros_last(list_num)}")
