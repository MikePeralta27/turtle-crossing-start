import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player_1 = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


screen.listen()
screen.onkey(player_1.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
