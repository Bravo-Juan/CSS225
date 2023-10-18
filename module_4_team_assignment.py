# Juan Bravo, Daniel Alvarez & Ramazan Tolonbaev
# 10/17/23
# Module 4 Team Activity

# Prompts the user to select a fruit to eat and informs them if the fruit they ate was healthy or poisonous

# Asks the user for their name before starting the challenge
username = input("Please tell me your name before continuing with the challenge:")

# Greets the user by their name and informs them to pick a fruit to eat
print("Hello {}, you must select a fruit to eat.".format(username))

# Informs the user about the possibility of selecting a poisonous fruit
print("Choose wisely as 3 out 6 of the fruits have poison inside of them.")

# Lists the different fruit options from number 1 to 6
print(" 1. Orange\n 2. Apple\n 3. Watermelon\n 4. Banana\n 5. Pineapple\n 6. Mango")

# Asks the user to select the number of the fruit that they want to eat
user_option = int(input("Please select the number of the fruit you would like to eat:"))

# Displays a message with positive news if the user selected 1, 4, or 6
if user_option == 1 or (user_option == 4) or (user_option == 6):
    print("You chose option {}, and it looks like you will live a happy and healthy life!".format(user_option))

# Displays a message with negative news if the user selected 2, 3, or 5
elif user_option == 2 or (user_option == 3) or (user_option == 5):
    print("You chose option {}, and it looks like you only have 24 hours left to live!".format(user_option))

# Displays a message that informs the user to select an appropriate number
else:
    print("Please select a fruit option between 1-6")