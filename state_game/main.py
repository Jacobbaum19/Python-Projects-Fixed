import turtle
import pandas as pd
from create_text import create_text

screen = turtle.Screen()
screen.title("U.S States Game")

# Image stuff
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Text stuff
text_turtle = turtle.Turtle()
text_turtle.hideturtle()  # Hide the turtle icon when it's only used for text
text_turtle.penup()


# User guesses list
user_guesses = []


# States CSV
states_and_x_y = pd.read_csv("50_states.csv")

# Convert state names in the DataFrame to lowercase for comparison
states_and_x_y['state'] = states_and_x_y['state'].str.lower()


# Game logic!
game_over = False
while not game_over:
    total_states = len(states_and_x_y["state"])
    answer_state = screen.textinput(title=f"Guess the State", prompt="What's another state name").lower()
    if answer_state == "stop":
        game_over = True
    elif answer_state in states_and_x_y['state'].values and answer_state not in user_guesses:
        user_guesses.append(answer_state)
        create_text(text_turtle, answer_state, states_and_x_y)  # Display text
        print(f"{answer_state} does exist, wow! So smart.")
    if len(user_guesses) == total_states:
        print("Congrats! You got them all!")
        game_over = True
    elif answer_state not in states_and_x_y['state'].values and answer_state != "stop":
        print(f"{answer_state} does not exist. Try again.")


# Creating empty map and filling it in.
# We can achieve this by running a while loop that will run until the empty list is equal to all 50 states
# We then export to a csv that will only contain the states they missed.

states_to_learn = set(states_and_x_y['state']) - set(user_guesses)

for remaining_state in states_to_learn:
    create_text(text_turtle, remaining_state, states_and_x_y)
print("Here's the states you missed!")

states_to_learn_df = pd.DataFrame(states_to_learn)

# Exporting to CSV
states_to_learn_df.to_csv("states_missed.csv", index=False)

screen.exitonclick()
