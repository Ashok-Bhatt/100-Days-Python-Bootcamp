from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-270,250)
        self.refresh_level(1)
    
    def refresh_level(self, level):
        self.clear()
        self.write(f"Level: {level}", font=FONT)
    
    def show_game_over(self):
        self.goto(0,0)
        self.write("Game Over", font=FONT)
    
    def show_game_won(self):
        self.goto(0,0)
        self.write("You Won", font=FONT)