# Juan Bravo
# 11/12/23

# Problem 1-Prompts the user to enter a value for the radius of the circle and calculates the area of the circle using the user's input.

import math

# This function calculates the area of a circle while using the math module
def areaOfCircle(r):
    area = math.pi * r ** 2
    rounded_area = round(area, 2)

    return rounded_area

# Prompts the user to enter the radius of the circle which then initiates the areaOFCircle function
r = int(input("Please enter the radius of the circle:"))

answer = areaOfCircle(r)

# Prints a message that mentions the radius that the user inputted and the area of the circle.
print("The area of a circle with a radius of {} is {}".format(r, answer))