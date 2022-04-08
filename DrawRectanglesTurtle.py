import turtle

def move(a, b):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)


def drawRectangle(a, b):
    for _ in range(2):
        move(a, b)

def drawrectangleColour(a, b, color):
    turtle.color(color)
    turtle.begin_fill()
    drawRectangle(a, b)
    turtle.end_fill()

turtle.speed(1)

drawRectangle(30, 60)
turtle.goto(86, -150)
drawrectangleColour(20, 50, 'red')
