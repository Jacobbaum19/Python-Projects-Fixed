from turtle import Turtle
import random

# List of Racing Turtles functions
class RacingTurtles:
    def __init__(self, colors):
        self.colors = colors
        self.turtles = self.make_racing_turtles()

    # Makes an empty list and a set Y-position at the left hand side of the screen. Makes a new turtle
    # It's given color and moves each turtle's Y-position by 60 every time it runs.

    def make_racing_turtles(self):
        turtles = []
        y_position = -230
        for color in self.colors:
            new_turtle = Turtle(shape="turtle")
            new_turtle.color(color)
            new_turtle.penup()
            new_turtle.goto(x=-280, y=y_position)
            y_position += 60
            turtles.append(new_turtle)
        return turtles

    # When a turtle reaches the 280 X cordinate (300 pixel screen - half of turtles width (20)),
    # Checks to see if the winning color matches the user bet and then stops the race.
    def start_race(self, user_bet):
        for turtle in self.turtles:
            random_distance = random.randint(1, 10)
            turtle.forward(random_distance)
            if turtle.xcor() > 280:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The winning {winning_color} turtle is the winner.")
                else:
                    print(f"You have lost! The winning {winning_color} turtle is the winner.")
                return False  # Stop the race
        return True
