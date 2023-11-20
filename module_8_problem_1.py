# Juan Bravo
# 11/19/23

# Prompts the user to enter two numbers and prints whether the numbers they entered are equal or not.

def userchoices_Evaluation():
    # Prompts user to enter a number.
    userchoice_1 = int(input("Enter a number:"))

    # Prompts user to enter another similar number.
    userchoice_2 = int(input("Enter another similar number:"))

    # Prints a message letting the user know that the numbers they picked are not equal.
    if userchoice_1 != userchoice_2:
        print("These are two different numbers, they are not equal.")

    # Prints a message letting the user know that the numbers they picked are equal.
    elif userchoice_1 == userchoice_2:
        print("These two numbers are the same, they are equal!")

userchoices_Evaluation()