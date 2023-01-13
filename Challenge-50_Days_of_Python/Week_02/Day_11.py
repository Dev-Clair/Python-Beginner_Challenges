# Day_11: Equal Strings


def main():
    """
        takes two arguments - strings
        compares if the have the same characters and equal length
        returns True is the above condition is satified else it should return False
    """
    while True:
        str_1 = input("\nEnter a string or character sequence: \t")
        str_2 = input("\nEnter another string or character sequence: \t")
        try:
            result = equal_strings(str_1, str_2)
        except ValueError:
            print("\nKindly Re-enter values.")
        else:
            print(result)
        print("\nDo you want to try again? yes or no")
        check_string = input("Choice: \t")
        if check_string == "no":
            break


def equal_strings(n, m):
    # Try using List Comprehension
    for i in range(0, len(n)):
        for j in range(1, len(n)):
            if n == m and len(n) == len(m):
                return "True"
            else:
                return "False"


main()


# Extra Challenge

def swap_values(new_list: list) -> list:
    """
        takes a list of numbers
        swaps the first element with the last
    """
    size = len(new_list)

    temp = new_list[0]
    new_list[0] = new_list[size - 1]
    new_list[size - 1] = temp
    return new_list


list_num = input("\nEnter numbers separated by whitespaces: \t").split()
print(swap_values(list_num))
