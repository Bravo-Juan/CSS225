# Juan Bravo
# 12/1/23

# Problem 3-Prompts the user to enter a number then stores the number in a list and adds them until the sum is over 100.

# Creates a list that stores the user's numbers.
user_numbers = []

total = 0

# Loops until the sum of the user's numbers is greater than 100.
while total < 100:
    user_number = int(input("Please enter a number: "))
    user_numbers += [user_number]
    total = 0
    for n in user_numbers:
        total += n

# Informs the user about the numbers they entered and that the sum of their numbers is over 100.
print("These are the numbers that you entered: {} and their sum is over 100.".format(user_numbers))

# Informs the use about the sum of the numbers they entered.
print("The sum of your numbers is {}.".format(total))