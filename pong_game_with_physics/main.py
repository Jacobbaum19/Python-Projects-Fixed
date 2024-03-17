from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

## TODO 1: Fix ball movement. Consider using the pythagorean theorem for the collision physics off the paddle.
## TODO 2: Add ball spin mechanics to the game

screen = Screen()
scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))
# Sending the paddles to the ball collision logic
ball.set_paddles(l_paddle, r_paddle)

# Sending missed shots to the ball class and then to scoreboard which updates the score and then
# clears the screen
ball.set_scoreboard(scoreboard)


# List of properties for the screen
# Width = 800, height = 600
# Black background and exit on click

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Creating the controls for the l and r paddle.

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Main game logic
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    # Collision with wall
    ball.ball_bonce_wall()
    # Detect collision with r and l paddle
    ball.ball_bonce_paddle()
    # Ball missing logic
    ball.ball_misses()
    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        game_is_on = False

if not game_is_on:
    scoreboard.write_winner()


screen.exitonclick()
