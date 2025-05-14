from turtle import Turtle, Screen
from random import randint 

class NewTurtle(Turtle):
    
    def __init__(self, color, x, y):
        Turtle.__init__(self, shape="turtle")
        self.up()
        self.color(color)
        self.goto(x, y)

screen = Screen()
screen.setup(height=400, width=500)
bet = screen.textinput(title="Enter your bet", prompt="Enter the color of turtle on which you will be betting")

color_list = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_coordinate = [-120, -80, -40, 0, 40, 80, 120]
turtle_list = []

for turtle in range(0,7):
    new_turtle = NewTurtle(color_list[turtle], -230, y_coordinate[turtle])
    turtle_list.append(new_turtle)

game_over = False
while not(game_over):
    for turtle in turtle_list:
        turtle.forward(randint(1,10))
        if turtle.xcor() > 230:
            if turtle.pencolor() == bet:
               print(f"You won! {turtle.pencolor()} turtle has won race. ")
            else:
                print(f"You loss! {turtle.pencolor()} turtle has won race. ")
            game_over = True
            break

screen.exitonclick()