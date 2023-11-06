# Juan Bravo
# 11/6/23

# Problem 2: Prints and odd integer between 0-100
import random

result = random.randint(0, 100)

# if result is divisble by 2 the result will increase by one making it into an odd integer
if result % 2 == 0:
    result += 1
    print(result)
# if result is an odd integer, it will be printed straightaway.
else:
    print(result)