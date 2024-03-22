from turtle import Turtle


# Code to create text.
# Grabs the state's row based off the user's response. If the state row is not empty. It finds
# the X and Y coordinates and the text moves to the state.
def create_text(written_text, user_guess, states_df):
    state_row = states_df[states_df["state"] == user_guess]
    if not state_row.empty:
        x = int(state_row["x"].iloc[0])
        y = int(state_row["y"].iloc[0])
        written_text.goto(x, y)
        written_text.write(user_guess)
