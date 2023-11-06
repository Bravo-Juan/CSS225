# Juan Bravo & Marissa Jones
# 10/31/23

# Prompts user to guess a number between 1-10 and displays a message if they guessed correctly or allows them to guess again and displays whether they guessed correctly or not the second time.

import random

answer = random.randint(1,10)

print("Please guess a number between 1 through 10:")
user_guess = int(input())

if user_guess != answer:
    if user_guess >= answer:
        print("Please guess lower!")
        user_guess = int(input())

    elif user_guess <= answer:
        print("Please guess higher!")
        user_guess = int(input())

if user_guess == answer:
    print("Congrats you guessed correctly, the answer was", answer)
else:
    print("Sorry, but you didn't guess correctly, the answer was", answer)