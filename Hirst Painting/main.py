import turtle
import random

# TODO: 1. Extract the colors from the jpg file.
def extract_colors(n_colors = 30):
    import colorgram
    colors = colorgram.extract('hirst_painting.jpg', n_colors)
    list_of_colors = []
    for _ in colors:
        r, g, b = _.rgb
        rgb_tuple = (r, g, b)
        list_of_colors.append(rgb_tuple)
    print(list_of_colors)

color_list = [(245, 241, 233), (227, 234, 242), (245, 234, 239), (233, 242, 236), (208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]

timmy = turtle.Turtle()
timmy.shape('turtle')
timmy.color('DeepPink')
turtle.colormode(255)
timmy.speed(0)
timmy.ht()
timmy.penup()
timmy.setposition(-200, -200)


# TODO: 2. Draw the Dots
def draw_dots(n_dots, colors):
    row_height = 50
    for _ in range(n_dots):
        color = random.choice(colors)
        timmy.dot(20, color)
        if _ % 10 == 9:
            # Move to the next row
            x_axis = -200
            y_axis = timmy.ycor() + row_height
            timmy.setposition(x_axis, y_axis)
        else:
            timmy.forward(50)

draw_dots(100, color_list)








screen = turtle.Screen()
screen.exitonclick()