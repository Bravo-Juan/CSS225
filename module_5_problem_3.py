# Juan Bravo
# 10/29/23

# Prompts the user to enter the number of sides, side length, line color, and fill color prior to drawing their polygon.

import turtle # Imports the "turtle" module

# Prompts the user to enter the of number sides, side length, line color, and fill color that they would like
side_number = int(input("How many sides would you like this polygon to have?"))

side_length = int(input("Please enter the side length of your polygon:"))

linecolor = input("What color would you like the sides of your polygon to be?")

fillcolor = input("What color would you like the inside of your polygon to be?")

screen = turtle.Screen() # Creates a turtle graphics screen
polygon = turtle.Turtle() # Creates a turtle object and enables drawing
polygon.pensize(4) # Changes the pen size (line thickness) of this turtle object
polygon.color(linecolor, fillcolor) # Changes the line color and fill color of this turtle object

polygon.up() # Lifts the pen which stops drawing
polygon.goto(-100,-100) # Repositions the drawing while being unable to draw
polygon.down() # Lowers the pen which enables drawing again

polygon.begin_fill() # Begins the fill color of the drawing
for i in range(side_number): # A loop used to draw the polygon according to the user's requests
    polygon.forward(side_length) # Moves the turtle forward according to the specific side length that the user chose
    polygon.left(360/side_number) # Draws the specific number of sides according the user's choice
polygon.end_fill() # Ends the filling processing by filling the drawing with the indicated color

screen.exitonclick() # Allows the user to close the graphics windows whenever they want