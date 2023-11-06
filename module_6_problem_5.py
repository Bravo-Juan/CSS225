# Juan Bravo
# 11/6/23

# Problem 5: Prompts the user to enter a value for radians and prints the user's value converted to degrees alongside the calculated value using the degrees function
import math

# Prompts user to enter a value for radians
print("Please enter a value for radians:")
radians = float(input())

# The formula to convert radians to degrees
degrees_calculation = radians * 180/math.pi

# The degrees function being used to convert radians to degrees
degrees = math.degrees(radians)

print("{} radians is equal to {} degrees!". format(radians, degrees_calculation))
print("According to a math function {} radians is equal to {} degrees!". format(radians, degrees))