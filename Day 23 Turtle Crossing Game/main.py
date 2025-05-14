import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, CAR_SPEED, MOVE_INCREMENT
from scoreboard import Scoreboard
from random import randint


def initialize_cars():
    car_list = []
    for _ in range(25):
        if (randint(0,1)):
            new_car = CarManager()
            new_car.place_cars(x = randint(-300,300), y = randint(-250,250))
            car_list.append(new_car)
    return car_list


def create_new_car(car_list):
    new_car = CarManager()
    new_car.place_cars(x = 300, y = randint(-260,280))
    car_list.append(new_car)

def delete_cars(car_list):
    for _ in range(0,len(car_list)):
        car_list[0].clear()
        del car_list[0]

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score_board = Scoreboard()

# Handling the movement of the player
screen.listen()
screen.onkey(key="Up", fun=player.move)

# Creating Initial Cars
car_list = initialize_cars()

# Setting some game variables
game_is_on = True
level = 1
car_speed = CAR_SPEED
acceleration = MOVE_INCREMENT

while game_is_on:

    time.sleep(1/car_speed)
    screen.update()

    # checking if the player has crossed the finishing line
    if player.ycor() > FINISH_LINE_Y:
        player.referesh_player()
        level = level + 1
        if level <= 5:
            score_board.refresh_level(level)
            car_speed = car_speed + acceleration
        else:
            game_is_on = False
            score_board.show_game_won()
    
    # Move all current cars
    for index, car in enumerate(car_list):
        car.move_car()
        if car.xcor() < -320:
            del car_list[index]

    # Checking collision with cars
    for car in car_list:
        if ( abs(car.xcor() - player.xcor()) <= 25 ) and ( abs(car.ycor() - player.ycor()) <=25 ):
            game_is_on = False
            score_board.show_game_over()
            break
    
    # Deciding whether a new car is going to be created and if yes then will create it
    if (not(randint(0,4))):
        create_new_car(car_list)

screen.exitonclick()