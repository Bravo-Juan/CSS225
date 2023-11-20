# Juan Bravo
# 11/10/23

# Takes a list and prints if the value 5 is in that list or not.

def listEvaluation(a_list):

    # Prints a specific message if the number 5 is in the list
    if 5 in a_list:
        print("The number 5 is in this list.")
    # Prints a specific message if the number 5 is not in the list
    else:
        print("The number 5 is not in this list.")
    return a_list

list_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
list_2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Calls the listEvaluation function and checks if 5 is in list_1
listEvaluation(list_1)

# Calls the listEvaluation function and checks if 5 is in list_2
listEvaluation(list_2)