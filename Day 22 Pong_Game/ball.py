from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        self.change_x = -10
        self.change_y = -10
        super().__init__(shape="circle")
        self.color("white")
        self.up()
    
    def move(self):

        new_x = self.xcor() + self.change_x
        new_y = self.ycor() + self.change_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.change_y = -1*self.change_y

    def bounce_x(self):
        self.change_x = -1*self.change_x

    def reset_game(self):
        self.goto(0,0)
        self.change_x = -1*self.change_x