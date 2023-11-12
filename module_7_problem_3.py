# Juan Bravo
# 11/12/23

# Problem 3-Multiplies all the numbers in a list. It uses the following list: [5, 2, 7, -1].

# This function multiplies all the numbers in a list.
def numMultiply(numberlist):
    result = 1
    for number in numberlist:
        result *= number

    return result

numberlist = [5, 2, 7, -1]
answer = numMultiply(numberlist)

# Prints a message that mentions the multiplication of all the numbers within the number list that was used.
print("The multiplication of all the numbers in the number list is {}".format(answer))