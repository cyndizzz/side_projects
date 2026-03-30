import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# TODO: 1. Create turtle and move it
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
i = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # TODO: 2. create cars and let them move
    car_manager.move()
    car_manager.add_car()

    # TODO: 3. Detect if the turtle reach the top edge, if so speed up the move_speed and level up.
    player.is_level_up()
    if player.is_lvl_up:
        scoreboard.increase_score()
        player.is_level_up()
        car_manager.level_up()

    # TODO: 4. Detect collision with the car, if so, game over and everything stops.
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()