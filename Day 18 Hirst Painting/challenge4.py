from turtle import Turtle, Screen
from random import randint


def generate_color():

    color = "#"

    for i in range(6):
        digit = randint(0,15)
        if digit<10:
            color = color + str(digit)
        else:
            color = color + chr(65+digit-10)

    return color


screen1 = Screen()

turtle1 = Turtle()
turtle1.turtlesize(0.5)
turtle1.pensize(5)
turtle1.speed(10)
turtle1.shape("circle")

for itr in range(250):

    color = generate_color()
    turtle1.pencolor(color)
    move = randint(1,4)

    if move==0:
        turtle1.forward(25)
    elif move==1:
        turtle1.backward(25)
    elif move==2:
        turtle1.left(90)
        turtle1.forward(25)
    else:
        turtle1.right(90)
        turtle1.forward(25)

screen1.exitonclick()