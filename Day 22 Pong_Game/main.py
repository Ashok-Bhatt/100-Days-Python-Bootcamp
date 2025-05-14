from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong Game")

screen.tracer(0)

# Creating two paddles in opposite directions and then showing them
left_paddle = Paddle(-370)
right_paddle = Paddle(370)
screen.update()

# Creating the ball
ball = Ball()

# Creating the Scoreboard
score_screen = ScoreBoard()

# Creating onkey click events
screen.listen()
screen.onkey(key="w", fun=left_paddle.move_upwards)
screen.onkey(key="s", fun=left_paddle.move_downwards)
screen.onkey(key="Up", fun=right_paddle.move_upwards)
screen.onkey(key="Down", fun=right_paddle.move_downwards)

game_on = True
is_hitted = False

while game_on:

    sleep(0.05)
    screen.update()
    ball.move()

    # Checking the collision with upper and lower boundary
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # checking if the ball has crossed the center or not
    if ball.xcor() >= -10 and ball.xcor() <= 10:
        is_hitted = False
    
    # Checking the collision with left paddle
    for segments in left_paddle.paddle_body:
        if (abs(ball.ycor()-segments.ycor())<=20 and ball.xcor()-segments.xcor()<=20):
            if not(is_hitted):
                ball.bounce_x()
                is_hitted = True
                break

    # Checking the collision with right paddle
    for segments in right_paddle.paddle_body:
        if (abs(ball.ycor()-segments.ycor())<=20 and segments.xcor()-ball.xcor()==20):
            if not(is_hitted):
                ball.bounce_x()
                is_hitted = True
                break

    # Checking if any of the paddles have missed the ball
    if ball.xcor() < -370 or ball.xcor() > 370:
        if ball.xcor() < -370:
            score_screen.right_point()
        else:
            score_screen.left_point()
        ball.reset_game()
        score_screen.update_score()
        left_paddle.reposition(-370)
        right_paddle.reposition(370)
    
    # Checking if any of the player loosed not
    if score_screen.left_score >=11 or score_screen.right_score>=11:
        game_on = False

screen.update()
sleep(2)
score_screen.show_game_winner()

screen.exitonclick()