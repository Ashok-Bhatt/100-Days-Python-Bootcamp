from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_SPEED = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__(shape="square")
        self.up()
        self.color(choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.setheading(180)
    
    def place_cars(self, x, y):
        self.goto(x, y)
    
    def move_car(self):
        self.forward(10)