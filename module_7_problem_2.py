# Juan Bravo
# 11/12/23

# Problem 2-Prompts the user to enter a number and outputs a message informing them whether their number is within my specific range.

# This function checks whether the number that the user entered is within a specific range and lets them know
def numberRange(userchoice):
    specific_range = range(1,10)
    if userchoice in specific_range:
        print("The number you chose is within my specific range.")
    else:
        print("The number you chose is not within my specific range.")

# Prompts the user to enter a number to find out if it's within a specific range
userchoice = int(input("Enter a number and find out if it's within my specific range:"))

result = numberRange(userchoice)

