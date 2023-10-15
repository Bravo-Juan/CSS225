# Juan Bravo
# 10/15/23

# Asks users for their name but only greets me and the professor

# Asks the user for their name
user_name = input("What is your name?")

# Displays a specific message if the user is named "Juan"
if user_name == "Juan":
    print("Hello,", user_name + ",", "it's great to see you.")

# Displays another specific message if the user is named "Robyn"
elif user_name == "Robyn":
    print("Hello,", user_name + ",", "it's nice to meet you.")

# Displays a different message if the user is not named "Juan" or "Robyn"
else:
    print(user_name + "?", "I don't believe we've met before.")