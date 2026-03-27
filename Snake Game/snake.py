import turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = turtle.Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        snake_length = len(self.segments)
        for i in range(snake_length-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].pos())
        self.head.forward(MOVE_DISTANCE)

    def go_north(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_south(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_east(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_west(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

