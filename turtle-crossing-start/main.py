import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(player.car_speed)
    screen.update()
    car.createcar()
    car.carmove()

# detect if car jam turtle
    for main_car in car.car_list:
        if main_car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()

#  detect if turtle at end of race successful crossing
    if player.at_endofline():
        player.back_to_start()
        scoreboard.increaselevel()


screen.exitonclick()