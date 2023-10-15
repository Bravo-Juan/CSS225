# Juan Bravo
# 10/15/23

# Computes the day of the week the user will return on if Sunday through Saturday were ordered from 0 through 6

# Asks the user to enter the day number that they will leave on
starting_day = int(input("From 0-6, What day number will you leave on?"))

# Asks the user to enter the number of days they will be out for
length = int(input("How long will your stay be?"))

# Computes the return day number that the user will return on
return_day = ((starting_day + length) % 7)

# Displays the day of the week that the user will return on according to their return day number
if return_day == 0:
    print("You will return on day", return_day, "which is Sunday!")
elif return_day == 1:
    print("You will return on day", return_day, "which is Monday!")
elif return_day == 2:
    print("You will return on day", return_day, "which is Tuesday!")
elif return_day == 3:
    print("You will return on day", return_day, "which is Wednesday!")
elif return_day == 4:
    print("You will return on day", return_day, "which is Thursday!")
elif return_day == 5:
    print("You will return on day", return_day, "which is Friday!")
elif return_day == 6:
    print("You will return on day", return_day, "which is Saturday!")
