# Juan Bravo
# 12/1/23

# Problem 2-Creates a list called L that contains the numbers 0 to 10.

# Creates an empty list named L.
L = []

counter = 0

# Loops until the counter is greater than 10.
while counter < 11:
    L = L + [counter]
    counter += 1

# Prints the completed list.
print(L)
