import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player_1 = Player()
cars_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_1.move, "Up")

n_cars = 0
game_is_on = True
while game_is_on:
    n_cars += 1
    time.sleep(0.1)
    screen.update()

    cars_manager.create_car()
    # move the cars
    cars_manager.move()

    for car in cars_manager.all_cars:
        # Detect collision with cars
        if car.distance(player_1) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect when Turtle has reached the top edge of the screen
    if player_1.is_at_the_finish_line():
        player_1.go_to_start()
        scoreboard.increase_level()
        cars_manager.increase_speed()


screen.exitonclick()
