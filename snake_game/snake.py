from turtle import Turtle
Move_Distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Notes for Super class (inheriting methods from other classes.)
# Put the name of the class inside the first class
# For example, SnakeFunctions(Ball):
# def __init__(self):
# super().__init__()


class SnakeFunctions:
    def __init__(self):
        self.segments = []
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake_body()
        self.head = self.segments[0]

    def create_snake_body(self):
        for position in self.starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Moves the snake by counting for the end of the segment list, similar to the extend function.
    # We use len to get the number of segments in the list.
    def snake_move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(Move_Distance)

    # Extends the snake by one starting from the last segment.
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
