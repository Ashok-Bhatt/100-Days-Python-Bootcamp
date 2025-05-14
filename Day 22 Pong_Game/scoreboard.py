from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        self.left_score = 0
        self.right_score = 0
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100,180)
        self.write(self.left_score, font=("courier",80,"normal"))
        self.goto(100,180)
        self.write(self.right_score, font=("courier",80,"normal"))
    
    def left_point(self):
        self.left_score = self.left_score + 1
    
    def right_point(self):
        self.right_score = self.right_score + 1

    def show_game_winner(self):
        self.clear()
        self.goto(0,0)
        if self.left_score > self.right_score:
            self.write("Left Person Won", font=("courier",40,"normal"), align="center")
        else:
            self.write("Right Person Won", font=("courier",40,"normal"), align="center")