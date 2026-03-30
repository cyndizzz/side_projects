from turtle import Turtle



class Score(Turtle):
    def __init__(self,paddle):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.score_display(paddle)

    def score_display(self, paddle):
        if paddle == "paddle_2":
            self.goto(-20, 250)
            self.write(f"{self.score}", align="right", font=("Courier", 30, "normal"))
        elif paddle == "paddle_1":
            self.goto(20, 250)
            self.write(f"{self.score}", align="left", font=("Courier", 30, "normal"))

    def add_score(self, paddle):
        self.score += 1
        self.score_display(paddle)

    def refresh(self, paddle):
        self.clear()
        self.score_display(paddle)
