from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.go_east, "Right")
screen.onkey(snake.go_west, "Left")
screen.onkey(snake.go_north, "Up")
screen.onkey(snake.go_south, "Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # TODO 4: Detect Collision w/ food
    if snake.head.distance(food) <15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        print("Score: ", scoreboard.score)

    # TODO 5: Detect Collision w/ wall
    if abs(snake.head.ycor()) >= 290 or abs(snake.head.xcor()) >=290 :
        scoreboard.reset()
        snake.reset()

    # TODO 6: Detect Collision w/ tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()