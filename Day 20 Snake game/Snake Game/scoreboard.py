from turtle import Turtle


class ScoreBoard(Turtle):
    
    def __init__(self):
        self.score = 0
        super().__init__()
        self.down()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("courier", 10, "bold"))
    
    def increment_score(self):
        self.score = self.score + 1

    def showGameOver(self):
        self.goto(0,0)
        self.write(f"Game Over!", font=("courier", 10, "bold"))