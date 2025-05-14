from turtle import Turtle,Screen

ashok = Turtle()
ashok.shape("turtle")
ashok.color("red")

screen = Screen()

length = 25
color = ["red","blue","green","yellow"]
for i in range(1,5):
    ashok.color(color[i-1])
    ashok.forward(length*i)
    ashok.right(90)
    ashok.forward(length*i)
    ashok.right(90)
    ashok.forward(length*i)
    ashok.right(90)
    ashok.forward(length*i)
    ashok.left(45)
    ashok.up()
    ashok.forward(25)
    ashok.left(45)
    ashok.down()