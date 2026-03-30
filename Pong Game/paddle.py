from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1


class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.penup()
        self.hideturtle()
        self.goto(x,0)
        self.showturtle()

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
