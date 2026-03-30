from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def add_car(self):
        random_chance = random.randrange(1,6)
        if random_chance == 1:
            car = Turtle('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            y_axis = random.randrange(-250, 250)
            car.goto(300, y_axis)
            self.cars.append(car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT