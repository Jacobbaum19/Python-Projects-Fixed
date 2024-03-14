from turtle import Screen
from racing_turtles_functions import RacingTurtles

### Note for self, every class with a . after is called a method not a function. ###


# Creates the screen and list of colors and is_race_on
screen = Screen()
screen.setup(width=600, height=500)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "pink"]
is_race_on = False


# Starts the turtle racing program! Makes the list of turtles
racing_turtles = RacingTurtles(colors)

user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race? Enter a color: ").lower()
print(f"User Bets: {user_bet}")

# Check if user_bet is a valid color
user_bet_is_valid = False
for turtle in racing_turtles.turtles:
    if user_bet == turtle.pencolor():
        user_bet_is_valid = True
        is_race_on = True
        break

if not user_bet_is_valid:
    print("That's not a right color.")
    # Listing the values of colors
    valid_colors = [turtle.pencolor() for turtle in racing_turtles.turtles]
    print(f"Valid colors are: {', '.join(valid_colors)}")


while is_race_on:
    is_race_on = racing_turtles.start_race(user_bet)


# Exits screen after click

screen.exitonclick()