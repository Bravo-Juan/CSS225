# Juan Bravo
# 11/6/23

# Problem 1-Prints 10 random integers from 25-35
import random

for i in range(10):
    random_number = random.randrange(25, 36)  # Will only generate integers between 25-35. 36 is not excluded.
    print(random_number)
