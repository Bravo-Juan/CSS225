# Juan Bravo
# 10/29/23

# A program that displays my first name in the middle of a unique frame.

import turtle # Imports the "turtle" module

screen = turtle.Screen() # Creates a turtle graphics screen
screen.bgcolor("Black") # Changes the background color of the graphics screen

frame = turtle.Turtle() # Creates a turtle object and enables drawing
frame.color("Aqua") # Changes the line color of this specific turtle object
frame.speed(75) # Changes the speed of this specific turtle object

# Repositions this turtle object while also enabling/disabling drawing in the process
frame.up()
frame.goto(210,-40)
frame.down()

# Loop used to draw this specific turtle object
for i in range(190):
    frame.left(131)
    frame.forward(350)
    frame.right(25)

juan = turtle.Turtle() # Creates another turtle object
juan.color("Gold") # Changes the line color of this specific turtle object
juan.pensize(4) # Changes the pen size (line thickness) of this specific turtle object
juan.speed(20) # Changes the speed of this specific turtle object

# Repositions the letter J while also enabling/disabling drawing in the process
juan.up()
juan.goto(-110,50)
juan.down()

# Draws the letter J
juan.forward(60)
juan.left(180)
juan.forward(30)
juan.left(90)
juan.forward(50)
juan.circle(-15,200)

# Repositions the letter U while also enabling/disabling drawing in the process
juan.up()
juan.goto(-30,50)
juan.down()

# Draws the letter U
juan.right(160)
juan.forward(52)
juan.circle(15,179)
juan.forward(52)

# Repositions the letter A while also enabling/disabling drawing in the process
juan.up()
juan.goto(25,-17)
juan.down()

# Draws the letter A
juan.forward(55)
juan.circle(-15,179)
juan.forward(55)
juan.backward(30)
juan.right(90)
juan.forward(30)

# Repositions the letter N while also enabling/disabling drawing in the process
juan.up()
juan.goto(75,-17)
juan.down()

# Draws the letter N
juan.right(90)
juan.forward(70)
juan.right(155)
juan.forward(80)
juan.left(155)
juan.forward(75)

screen.exitonclick() # Allows the user to close the graphics windows whenever they want