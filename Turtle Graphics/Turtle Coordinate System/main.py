import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

all_racers =[]
for _ in range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.color(colors[_])
    tim.penup()
    y_axis = -100 + _*30
    tim.goto(x=-230, y=y_axis)
    all_racers.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_racers:
        if turtle.xcor() > 200:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()