from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from time import sleep

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

game_score = ScoreBoard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True

while game_on:

    # Updating the snake positions
    screen.update()
    sleep(0.05)
    snake.move()

    # Checking if snake has eaten food or not
    if snake.head.distance(food)<20:
        food.refresh()
        game_score.increment_score()
        game_score.refresh_score()
        snake.enlarge_snake()
    
    # Checking collision of snake with walls
    if (snake.head.xcor()<-300 or snake.head.ycor()<-300 or snake.head.xcor()>300 or snake.head.ycor()>300):
        game_on = False

    # Checking collision of snake head with it's body
    for segment in snake.turtle_list[1:]:
        if (snake.head.distance(segment)  < 10):
            game_on = False

game_score.showGameOver()

screen.exitonclick()