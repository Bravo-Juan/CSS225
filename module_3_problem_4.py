# Juan Bravo
# 10/15/23

# Computes the area of a circle after given the radius by the user

# Asks the user to enter the radius
radius = float(input("In order to calculate the area of the circle, please provide the radius:"))

# Calculates the area of the circle
area = (3.1416 * radius ** 2)

# Displays the area of the circle with a nice message
print("Looks like the area of the circle is", round(area, 2))
