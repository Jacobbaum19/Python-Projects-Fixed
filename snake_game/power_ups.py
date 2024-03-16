from turtle import Turtle
import random
Seconds = 3000
class AddTwo(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("purple")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.move_every_x_seconds(Seconds)  # Move to a new position every 3 seconds

    def move_power_up(self):
        """Move the power-up to a new, random location."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.move_every_x_seconds(Seconds)  # Schedule the next move

    def move_every_x_seconds(self, milliseconds):
        """Schedule the power-up to move to a new location every specified milliseconds."""
        screen = self.getscreen()
        screen.ontimer(self.move_power_up, milliseconds)

    def refresh(self):
        """Immediately move the power-up to a new location."""
        self.move_power_up()
