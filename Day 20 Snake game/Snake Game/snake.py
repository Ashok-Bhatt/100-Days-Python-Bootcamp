from turtle import Turtle

COORDINATES = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]
    
    def create_snake(self):
        for turtle in range(0,3):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.up()
            new_turtle.goto(COORDINATES[turtle][0], COORDINATES[turtle][1])
            self.turtle_list.append(new_turtle)


    def move(self):
        for turtle in range(len(self.turtle_list)-1, 0, -1):
            new_x = self.turtle_list[turtle-1].xcor()
            new_y = self.turtle_list[turtle-1].ycor()
            self.turtle_list[turtle].goto(new_x, new_y)
        self.head.forward(20)

    def enlarge_snake(self):
        x = self.turtle_list[-1].xcor()
        y = self.turtle_list[-1].ycor()
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.up()
        new_turtle.goto(x,y)
        self.turtle_list.append(new_turtle)

    def up(self):
        if self.head.heading()!=DOWN:
            self.turtle_list[0].setheading(UP)
    
    def down(self):
        if self.head.heading()!=UP:
            self.turtle_list[0].setheading(270)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.turtle_list[0].setheading(180)

    def right(self):
        if self.head.heading()!=LEFT:
            self.turtle_list[0].setheading(0)