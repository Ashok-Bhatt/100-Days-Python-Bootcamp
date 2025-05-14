from turtle import Turtle, Screen

screen1 = Screen()
turtle1 = Turtle()

for side in range(3,11):
    for turn in range(side):
        turtle1.forward(100)
        turtle1.right(360/side)

screen1.exitonclick()