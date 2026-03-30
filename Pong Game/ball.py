from turtle import Turtle
from random import randint, choice

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.refresh()

    def refresh(self):
        self.goto(0,0)

        r = choice([(-60, 60), (120, 240)])
        angle= randint(*r)
        self.setheading(angle)
        self.forward(10)

    def move(self):
        self.speed("fast")
        self.forward(10)

    def bounce(self, object):
        current_angle = self.heading()

        if object == "wall":
            new_angle = 360 - current_angle
        elif object == "paddle_1":
            new_angle = (540 - current_angle) % 360
        elif object == "paddle_2":
            new_angle = current_angle - 90
        else:
            new_angle = current_angle
        self.setheading(new_angle)

