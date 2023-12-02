# Juan Bravo
# 12/1/23

# Problem 4-Initializes a counter at 0 and runs to 50. Each number that is divisible by 10 is put into a list named tens.

# Creates a list that stores every number that is divisible by 10.
tens = []

counter = 0

# A loop that runs until the counter reaches 50.
while counter < 51:

    # If a number is divisible by 10 it's placed into the list named "tens".
    if counter % 10 == 0:
        tens += [counter]
    counter += 1

# Displays the list with all the numbers that are divisible by 10 from 0 to 50.
print("These numbers are divisible by 10 {}.".format(tens))