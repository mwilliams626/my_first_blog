from turtle import *
import math

t = Turtle()

x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)





sides = 4
angle = 90
while sides > 0:
    t.pendown()
    t.left(angle)
    t.forward(50)
    t.penup()
    sides = sides - 1
