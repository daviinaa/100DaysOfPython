from turtle import Turtle
import time

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = 0.1
        self.shape("turtle")
        self.color("Hotpink")
        self.setheading(90)
        self.pu()
        self.back_to_start()

    def back_to_start(self):
        self.goto(STARTING_POSITION)
        self.car_speed *= 0.4

    def move(self):
        self.forward(MOVE_DISTANCE)

    def at_endofline(self):
        if self.ycor() > FINISH_LINE_Y:
            return True



