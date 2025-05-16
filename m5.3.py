# Name: Erbol Zamirov
# Date: May 16, 2025

# This program asks the user for polygon information and draws it using turtle graphics

import turtle

# Get user input
sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length of each side: "))
line_color = input("Enter the line color: ")
fill_color = input("Enter the fill color: ")

# Set up turtle
pen = turtle.Turtle()
pen.color(line_color, fill_color)
pen.begin_fill()

# Draw polygon
angle = 360 / sides
for _ in range(sides):
    pen.forward(length)
    pen.left(angle)

pen.end_fill()
turtle.done()