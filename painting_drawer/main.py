from random import choice
import turtle
from random_functions import random_color, random_spot_choice, rgb_to_hex

# Sets up Tim's attributes and changes the color mode to accept rgb values from color list.
tim = turtle.Turtle()
tim.shape("turtle")
turtle.colormode(255)
tim.speed(8)
num_dots = 10
num_dots_placed = 0
row_number = 0


# Set starting position to bottom left corner and pickup the pen, so it does not draw on its way over.
# As well setting up the screen
screen = turtle.Screen()
screen.setup(width=500, height=500)  # Set screen size
tim.penup()
tim.goto(-750, -400)  # Set coordinates for the bottom left corner
tim.pendown()

starting_position = tim.position()  # Get the starting position

# Draw a row of dots
def draw_row_of_dots():
    global num_dots_placed  # Declare num_dots_placed as a global variable
    for _ in range(num_dots):  # Use num_dots instead of 30
        if random_spot_choice():
            tim.pencolor(random_color())
            tim.dot(20)
            num_dots_placed += 1
            print(num_dots_placed)
        tim.penup()
        tim.forward(50)

# Draw multiple rows of dots
for _ in range(20):
    while row_number != 10:
        draw_row_of_dots()
        starting_position = (starting_position[0], starting_position[1] + 50)
        row_number += 1
        print(row_number)
        tim.goto(starting_position)  # Update y-coordinate for the next row



tim.hideturtle()
screen = turtle.Screen()
screen.exitonclick()
