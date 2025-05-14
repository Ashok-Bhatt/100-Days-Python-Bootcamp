from turtle import Turtle

class Paddle:

    def __init__(self, x_coor):
        self.x_coor = x_coor
        self.paddle_body = []
        self.create_paddle()
    
    def create_paddle(self):
        for paddle_segment in range(0,5):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.up()
            segment.goto(self.x_coor, paddle_segment*20-50)
            self.paddle_body.append(segment)
    
    def move_downwards(self):
        for paddle_segment in self.paddle_body:
            new_x = paddle_segment.xcor()
            new_y = paddle_segment.ycor() - 20
            paddle_segment.goto(new_x, new_y)
    
    def move_upwards(self):
        for paddle_segment in self.paddle_body:
            new_x = paddle_segment.xcor()
            new_y = paddle_segment.ycor() + 20
            paddle_segment.goto(new_x, new_y)
    
    def reposition(self, x_coor):
        for paddle_portion, paddle_segment in enumerate(self.paddle_body):
            paddle_segment.goto(x_coor, paddle_portion*20-50)