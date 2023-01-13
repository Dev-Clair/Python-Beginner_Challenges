# Day_06: User Name

def main():
    while True:
        print("\nPlease enter your email to get started.")
        email = input("\ne-mail: \t")
        username = user_name(email)
        print(f"\nYour username is {username}")
        print("Will you like to try another email? yes or no")
        Try_Again = input("\nChoice? ").lower()
        if Try_Again == "no":
            break
    print(
        f"\nCongratulations!, You have successfully created your username {username}")


def user_name(value: str) -> str:
    """
        Function called user_name
        generates username from user's email
    """

    return value.rstrip("@gmail.com")[::]


if __name__ == "__main__":
    main()

    # Extra Challenge

value_input = [2, 5, 7, 8, 9]


def zeroed(n: list):
    """
        A function that takes one argument - a list of integers
        zeros the first and last elements
    """
    n[0] = 0
    n[len(n)-1] = 0
    return n


print(zeroed(value_input))
