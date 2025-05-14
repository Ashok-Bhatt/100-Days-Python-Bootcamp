from turtle import Turtle, Screen

sc1 = Screen()
t1 = Turtle()

for turn in range(4):
    t1.forward(100)
    t1.right(90)

sc1.exitonclick()