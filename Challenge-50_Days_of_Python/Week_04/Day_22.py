# Day_22: Add Underscore

def add_hash(val_1: str) -> str:
    """
        takes a string input
        adds the hash bang "#" between the words
        returns a formatted string output
    """
    return f"{('#').join(val_1)}"


def add_underscore(val_2: str) -> str:
    """
        takes a string input
        replaces # between the words with _
        returns a formatted string output
    """
    return f"{val_2.replace('#', '_')}"


def remove_underscore(val_3: str) -> str:
    """
        takes a string input
        replaces _ between the words with " "
        returns a formatted string output
    """
    return f"{val_3.replace('_', '')}"


user_input = input("\nEnter a word: \t")
print(add_hash(user_input))
print(add_underscore(add_hash(user_input)))
print(remove_underscore(add_underscore(add_hash(user_input))))
