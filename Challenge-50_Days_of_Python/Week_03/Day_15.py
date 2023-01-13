"""
   Function called same_in_reverse
   checks if a string checks same in reverse
   keeps checking until user enters wrong input
"""


def same_in_reverse():
    while True:
        user_input = input("\nEnter a word:\t")
        if user_input == user_input[::-1]:
            print("True")
        else:
            print("False")
        print("\nDo you want to try another name? yes or no")
        input_word = input("Choice: \t")
        if input_word == "no":
            break


same_in_reverse()


# Extra Challenge
names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}


def your_age():
    name = input("\nPlease enter your name: \t").lower()
    for key in names_age.keys():
        if key == name:
            return f"\nHi, {name}, you are {names_age.get(key)} years old."
    else:
        while name not in names_age.keys():
            print(f"I'm sorry, {name} is not in the database.")
            age = int(input("\nPlease enter your age: \t").lower())
            names_age.update({name: age})
            return f"Hi, {name}, you are {names_age.get(name)} years old."


your_age()
