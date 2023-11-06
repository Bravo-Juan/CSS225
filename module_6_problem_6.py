# Juan Bravo
# 11/6/23

# Problem 6: Prompts the user to enter a positive number and prints the factorial of the user's number alongside the calculated factorial using the factorial function
import math

# Prompts the user to enter a positive number
user_input = int(input("Please enter a positive number:"))

factorial = 1

# A for loop that calculate the factorial of the user's input
for i in range (1, user_input + 1):
    factorial *= i

# The factorial function being used to calculate the factorial of the user's input
factorial_function = math.factorial(user_input)

print("The factorial of {} is {}".format(user_input, factorial))
print("According to a math function the factorial of {} is {}". format(user_input, factorial_function))