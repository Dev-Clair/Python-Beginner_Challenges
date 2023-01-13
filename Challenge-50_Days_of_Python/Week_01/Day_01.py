# Day_01: Division and Square-root
def main():
    while True:
        user_input = int(input("Enter a number: "))
        result = divide_or_square(user_input)
        print(f"\nThe result is {result}")
        print("\nDo you want to try another value? yes or no")
        try_another_value = input("\nChoice: \t")
        if try_another_value == "no":
            break


def divide_or_square(user_input: int):
    from math import sqrt
    """
         takes an argument - an integer
         performs specified operation and
         returns output to the caller
    """
    if user_input % 5 == 0:
        return sqrt.user_input
    elif user_input % 5 != 0:
        return user_input % 5


if __name__ == "__main__":
    main()


# Extra Challenge

automobile = {"truck": "hilux", "sedan": "mercedez",
              "suv": "hyundai", "trailer": "iveco", "heavy-duty": "backacter"}


def longest_value(n):
    """
    takes a dictionary as an argument
    returns the longest value
    """
    return max(n, key=len)


# pass automobile to longest_value function
result = longest_value(automobile)
# use the dictionary get method to retrieve the value paired to the returned value
print(f"\nThe longest value is {automobile.get(result)}")
