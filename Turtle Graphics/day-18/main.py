from turtle import Turtle, Screen, colormode    # https://docs.python.org/3/library/turtle.html
from random import randint, choice
import colorgram

timmy = Turtle()
timmy.shape('turtle')
timmy.color('DeepPink')         # Reference: https://cs111.wellesley.edu/reference/colors; https://trinket.io/docs/colors
colormode(255)
timmy.speed(0)
# timmy.forward(100)
# timmy.right(90)

# TODO: 1. Draw a Square

def draw_square(steps):
    for _ in range(4):
        timmy.forward(steps)
        timmy.left(90)
# draw_square(100)

# TODO: 2. Draw a Dashed Line
def draw_dashed_line(steps, dash_width):
    for _ in range(10):
        # Option 1
        # timmy.forward(steps/10)
        # current_x = timmy.xcor()
        # new_x = timmy.xcor() + dash_width
        # timmy.teleport(new_x,0.00)

        # Option 2
        timmy.forward(dash_width)
        timmy.up()
        timmy.forward(dash_width)
        timmy.down()

# draw_dashed_line(50, 10)

# TODO: 5. Generate Random Color
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

# TODO: 3. Draw Different Shapes
def draw_shape(steps, turns):
    """Draw different shapes based on the number of turns, with a random color"""
    timmy.pencolor(random_color())
    angel = 360 / turns
    for _ in range(turns):
        timmy.forward(steps)
        timmy.right(angel)

# for side in range(3,11):
#     draw_shape(100, side)

# TODO: 4. Draw a Random Walk
def random_walk(steps):
    distance = 20
    angles = [0, 90, 180, 270]
    timmy.pensize(3)
    for _ in range(steps):
        timmy.pencolor(random_color())
        direction = choice(angles)
        timmy.forward(distance)
        timmy.setheading(direction)

# random_walk(30)

# TODO: 6. Make a Spirograph
def draw_spirograph(n):
    angles = 360 / n
    for _ in range(n):
        timmy.pencolor(random_color())
        timmy.setheading(timmy.heading() + angles)
        timmy.circle(50)

# draw_spirograph(10)


# TODO: 7. Hirst Painting Project



















screen = Screen()
screen.exitonclick()