import random
from turtle import Turtle

FOOD_SIZE_WIDTH, FOOD_SIZE_LEN = 0.5,0.5
SCREEN_WIDTH, SCREEN_HEIGHT = 560, 560

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(FOOD_SIZE_WIDTH, FOOD_SIZE_LEN)
        self.color("blue")
        self.refresh()


    def refresh(self):
        xcor = random.randint(int(-SCREEN_WIDTH / 2), int(SCREEN_WIDTH / 2))
        ycor = random.randint(int(-SCREEN_HEIGHT / 2), int(SCREEN_HEIGHT / 2))
        self.goto((xcor, ycor))