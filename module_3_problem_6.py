# Juan Bravo
# 10/15/23

# Converts degrees Fahrenheit to degrees Celcius

# Asks users to enter the temperature in Fahrenheit
degrees_fahrenheit = float(input("What is the temperature in fahrenheit?"))

# Converts degrees Fahrenheit to degrees Celcius
degrees_celcius = ((degrees_fahrenheit - 32) * 5/9)

# Displays the degrees Fahrenheit converted to degrees Celcius
print(degrees_fahrenheit, "degrees Fahrenheit is", round(degrees_celcius, 1), "degrees Celcius!")