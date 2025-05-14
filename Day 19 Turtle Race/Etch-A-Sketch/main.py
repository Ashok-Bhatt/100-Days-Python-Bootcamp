from turtle import Turtle, Screen


def forward():
    t1.forward(10)


def backward():
    t1.backward(10)


def clockwise():
    t1.right(10)


def anticlockwise():
    t1.left(10)


def clearscreen():
    t1.clear()
    t1.penup()
    t1.home()
    t1.pendown()

s1 = Screen()
t1 = Turtle()

s1.listen()
s1.onkey(key="w", fun=forward)
s1.onkey(key="s", fun=backward)
s1.onkey(key="a", fun=anticlockwise)
s1.onkey(key="d", fun=clockwise)
s1.onkey(key="c", fun=clearscreen)
s1.exitonclick()