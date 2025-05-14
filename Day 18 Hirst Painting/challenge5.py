from turtle import Turtle, Screen
from random import randint


def get_color():
    
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
turtle1.speed(50)
turtle1.shape("circle")

for i in range(360):
    turtle1.pencolor(get_color())
    turtle1.circle(50)
    turtle1.left(1)

screen1.exitonclick()