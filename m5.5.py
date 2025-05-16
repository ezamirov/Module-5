# Name: Erbol Zamirov
# Date: May 16, 2025

# This program uses turtle graphics to draw a colorful spiral star pattern

import turtle
import colorsys

screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)
screen.bgcolor("black")

# Create colorful spiral star
colors = 36
hue = 0
for i in range(360):
    col = colorsys.hsv_to_rgb(hue, 1, 1)
    pen.color(col)
    pen.forward(i * 3 / colors + i)
    pen.left(59)
    pen.width(i * colors / 200)
    hue += 0.005

turtle.done()