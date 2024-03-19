import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating instances of the car manager and scoreboard to send to the player.py that does most of the
# heavy lifting.
car_manager = CarManager()
scoreboard = Scoreboard()
player = Player(car_manager, scoreboard)


# Controls
screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
# Main logic of the game
while game_is_on:
    time.sleep(0.1)
    # Logic for spawning the cars and respawning them after they reach the left edge of the screen
    if player.ycor() < 280:
        car_manager.spawn_car()
        car_manager.move_car()
        car_manager.delete_car()
    # Resets player after they reach the end.
    player.next_level()
    # Player gets hit
    if player.player_get_hit():
        scoreboard.game_over()
        game_is_on = False
    screen.update()


# When game is over...
screen.exitonclick()
