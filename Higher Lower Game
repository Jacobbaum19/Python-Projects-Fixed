"""Importing the various libaries including clear, random and the game_data and art from the other modules."""
from art import vs, you_lose, logo
from game_data import data
import random
from replit import clear

# Global Variables
game_over = False
user_score = 0

def random_selector():
    """Select a random entry from the data."""
    return random.choice(data)

def comparison(first_entry, second_entry, user_input):
    """Compare two entries based on user input and updates user score if they got it right. Otherwise, the game is over"""
    global game_over, user_score
    if user_input == "a" and first_entry['follower_count'] > second_entry['follower_count'] or \
       user_input == "b" and second_entry['follower_count'] > first_entry['follower_count']:
        user_score += 1
        # Update first_entry to second_entry and get a new random second_entry
        return second_entry, random_selector(), False
    else:
        game_over = True
        return first_entry, second_entry, True  # Game over, return entries without changes

def start_game():
    """Start the higher-lower game. Made the game_over and user_score function global to update the score after each iteration of the comparsion function. Made it so the first_entry and second_entry never can match each other. """
    global game_over, user_score
    print(logo)
    first_entry = random_selector()
    second_entry = random_selector()
    while second_entry == first_entry:
        second_entry = random_selector()
    game_over = False

    while not game_over:
        print(f"Compare A: {first_entry['name']}, a {first_entry['description']}, from {first_entry['country']}")
        print(vs)
        print(f"Against B: {second_entry['name']}, a {second_entry['description']}, from {second_entry['country']}")
        user_input = input("Who has more followers? Type 'A' or 'B': ")
        print(f"Current score: {user_score}")
        first_entry, second_entry, game_over = comparison(first_entry, second_entry, user_input.lower())
        if not game_over:
            clear()
        else:
            clear()
            print(you_lose)
            print(f"Final score: {user_score}")
            print(f"{first_entry['name']} has {first_entry['follower_count']} million followers")
            print(f"{second_entry['name']} has {second_entry['follower_count']} million followers")

start_game()
