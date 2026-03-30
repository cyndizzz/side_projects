from turtle import Turtle

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pensize(5)
        self.penup()
        self.hideturtle()
        self.draw_dash_line(SCREEN_HEIGHT)
        self.score = 0

    def draw_dash_line(self, length):
        self.goto(0, -290)
        self.setheading(90)
        distance = 20
        pairs = int(length / distance / 2 )
        for l in range(pairs):
            self.pendown()
            self.forward(distance)
            self.penup()
            self.forward(distance)


