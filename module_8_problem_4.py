# Juan Bravo
# 11/10/23

# Prompts the user to enter a year and informs them if the year they entered is a leap or not.

def yearEvaluation(year):
    leap = False

    # Determines if the year that was entered is a leap year or not.
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap

# Prompts the user to enter a year.
year = int(input("Enter a year:"))

# Call the yearEvaluation function and determine if the year that was entered by the user is a leap year or not.
result = yearEvaluation(year)

# prints a specific message if the year that was entered is a leap year or not.
if result == True:
    print("{} is a leap year.".format(year))
else:
    print("{} is not a leap year.".format(year))