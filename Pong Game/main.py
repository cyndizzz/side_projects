# Game plan

# Board: 2 independent scores + divide
# Pong paddle: 2 independent paddle
# Pong ball: 1 ball

from turtle import Screen
from board import Board
from paddle import Paddle
from ball import Ball
from score import Score
import time

# TODO 1: Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

board = Board()

# TODO 2: Create and move a paddle
paddle_1 = Paddle(350)
score_1 = Score('paddle_1')
screen.listen()
screen.onkey(paddle_1.move_up, 'Up')
screen.onkey(paddle_1.move_down, 'Down')

# TODO 3: Create another paddle
paddle_2 = Paddle(-350)
score_2 = Score('paddle_2')
screen.onkey(paddle_2.move_up, 'w')
screen.onkey(paddle_2.move_down, 's')

# TODO 4: Create and move the ball
ball = Ball()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

# TODO 5: Detect collision w/ wall and bounce
    if abs(ball.ycor()) > 270:
        ball.bounce('wall')

# TODO 6: Detect collision w/ paddle
    if (paddle_1.xcor() - ball.xcor() <= 10) and abs(ball.ycor() - paddle_1.ycor()) <= 50:
        ball.bounce('paddle_1')
    elif (ball.xcor() - paddle_2.xcor() <= 10) and abs(ball.ycor() - paddle_2.ycor()) <= 50:
        ball.bounce('paddle_2')

    ball.move()

# TODO 7: Detect when paddle misses
    if paddle_1.xcor() < ball.xcor():
        score_2.add_score('paddle_2')
        score_2.refresh('paddle_2')
        ball.refresh()
    elif paddle_2.xcor() > ball.xcor():
        score_1.add_score('paddle_1')
        score_1.refresh('paddle_1')
        ball.refresh()

# TODO 8: Keep score




screen.exitonclick()