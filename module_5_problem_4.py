# Juan Bravo
# 10/29/23

# Iterates the integers from 1 to 50 and displays a specific message if the number is divisible by three, five or both.

for i in range(1, 51): # Iterates the integers from 1 to 50
    if i % 3 == 0: # Prints "Divisible by three" if the number is divisible by three
        print("Divisible by three")
    elif i % 5 == 0: # Prints "Divisible by five" if the number is divisible by five
        print("Divisible by five")
    elif i % 3 == 0 and i % 5 == 0: # Prints "Divisible by both" if the number is divisible by three and five
        print("Divisible by both")
    else: # Prints the number if it's not divisible by three or five
        print(i)