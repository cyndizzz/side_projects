from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.is_lvl_up = False


    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_level_up(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.is_lvl_up = True
        else:
            self.is_lvl_up = False

