# Juan Bravo
# 11/19/23

# Prompts the user to enter two numbers and prints whether the sum of their numbers is greater than, less than, or equal to 10.

def number_Comparison():
    # Prompts the user to enter a number of their choice.
    userchoice_1 = float(input("Enter any number of your choice:"))

    # Prompts the user to enter a number of their choice.
    userchoice_2 = float(input("Enter another number of your choice:"))

    # Adds the two numbers that the user entered.
    choice_total = userchoice_1 + userchoice_2

    # Prints a message letting the user know that the sum of their numbers is greater than 10.
    if choice_total > 10:
        print("The sum of your numbers is {} and it's greater than 10!".format(choice_total))

    # Prints a message letting the user know that the sum of their numbers is less than 10.
    elif choice_total < 10:
        print("The sum of your numbers is {} and it's less than 10!".format(choice_total))

    # Prints a message letting the user know that the sum of their numbers is equal to 10.
    elif choice_total == 10:
        print("The sum of your numbers is {} and it's equal to 10!".format(choice_total))

number_Comparison()