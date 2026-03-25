# from turtle import Turtle, Screen, begin_fill, end_fill, forward, left, right, up, down
from turtle import *
# Reference:
# Turtle command: https://docs.python.org/3/library/turtle.html
# Turtle colors: https://cs111.wellesley.edu/reference/colors


# turtle is the module, Turtle is the blueprint, aka class.

# create a new object from blueprint
timmy = Turtle()
print(timmy)

# Call methods, that are associated with the object
timmy.shape('turtle')
# TODO: 1. Change the color
timmy.color('DeepPink')     # Change the color
# TODO: 2. Move the turtle forward by 100 paces
timmy.forward(100)

my_screen = Screen()
# Tap into the attribute, by using {object_name}.{attribute}
print(my_screen.canvheight)
my_screen.exitonclick()



