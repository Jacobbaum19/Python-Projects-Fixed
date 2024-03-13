from random import choice
import turtle
from random_functions import random_color, random_spot_choice, rgb_to_hex

tim = turtle.Turtle()
tim.shape("turtle")
num_dots = 10
num_dots_placed = 0


def draw_row_dots():
    # Draw the first row of dots
    for _ in range(30):
        if random_spot_choice():
            tim.pencolor(rgb_to_hex(random_color()))
            tim.dot(20)
            num_dots_placed += 1
            print(num_dots_placed)
        tim.penup()
        tim.forward(50)
