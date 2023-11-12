# Juan Bravo
# 11/12/23

# Problem 4-Takes a list of numbers and returns a new list with unique elements of the first list.

# This function uses the first list and returns a new list with unique elements from the first one.
def listConversion(current_list):
    new_list = []
    for number in currentlist:
        if number not in new_list:
            new_list.append(number)

    return new_list

currentlist = [1, 3, 3, 3, 6, 2, 3, 5]
result = listConversion(currentlist)

# Outputs the new list with unique elements of the first list
print(result)