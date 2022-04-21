from turtle import *

bgcolor('black')
speed(0)
hideturtle()
for i in range(240):
    color('red')
    circle(i * 1.2)
    color('orange')
    circle(i)
    right(3)
    forward(3)
done()
