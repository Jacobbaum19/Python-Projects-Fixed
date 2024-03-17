from turtle import Turtle

# Paddle attributes

"""This code contains the logic for the paddle."""


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)

    # Paddle moving controls
    def go_up(self):
        if self.ycor() < 210:
            new_y = self.ycor() + 50
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -210:
            new_y = self.ycor() - 50
            self.goto(self.xcor(), new_y)
