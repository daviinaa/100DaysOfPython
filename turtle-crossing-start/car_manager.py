import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.x_move = MOVE_INCREMENT
        self.car_list = []
        self.car_num = 10

    def createcar(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.pu()
            car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-230, 230)
            car.goto(300, random_y)
            self.car_list.append(car)

    def carmove(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE)




