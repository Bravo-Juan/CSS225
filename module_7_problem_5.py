# Juan Bravo
# 11/12/23

# Problem 5-Draws an innermost square and four additional squares around it, with each square outside the previous one

import turtle

# Draws the innermost square
def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

# Draw the four additional squares around the innermost square
def draw_additional_squares(t, number_of_squares, sz):
    for i in range(number_of_squares):
        drawSquare(alex, sz + i * 20)
        t.penup()
        t.goto(-10 * (i + 1), -10 * (i + 1))
        t.pendown()

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

# The values that draw the additional squares around the innermost square.
draw_additional_squares(alex, 5, 20)

wn.exitonclick()