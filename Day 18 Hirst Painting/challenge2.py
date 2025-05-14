from turtle import Turtle, Screen

screen1 = Screen()
turtle1 = Turtle()

for moves in range(25):
    turtle1.forward(5)
    turtle1.up()
    turtle1.forward(5)
    turtle1.down()

screen1.exitonclick()