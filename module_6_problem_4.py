# Juan Bravo
# 11/6/23

# Problem 4: Prints an approximation of pi alongside the value the actual value of pi
import math

# The number of terms that would be used in the formula
number_approximation = 1000000

approximation_of_pi = 0

denominator = 1

# if i is even then the term is added to the approximation using 4/demominator while also increasing the denominator by 2
for i in range(number_approximation):
    if i % 2 == 0:
        approximation_of_pi += 4/denominator
        denominator += 2

# if if is odd then the term is subtracted to the approximation using 4/demominator while also increasing the denominator by 2
    else:
        approximation_of_pi -= 4/denominator
        denominator +=2

print("The approximation of pi is", approximation_of_pi)
print("The value of pi is", math.pi)