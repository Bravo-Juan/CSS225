# Juan Bravo
# 10/15/23

# Computes the MPG for a vehicle after given the miles driven and gallons used by the user.

# Asks the user to enter the number of miles they drove
miles_driven = float(input("How many miles did you drove?"))

# Asks the user to enter the number of gallons that they used
gallons_used = float(input("How many gallons did you use?"))

# Calculates the MPG of the vehicle
mpg = (miles_driven / gallons_used)

# Displays the MPG for the user's vehicle with a nice message
print("Looks like your vehicle's MPG is", round(mpg, 1), "miles per gallon.")