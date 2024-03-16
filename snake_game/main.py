from turtle import Screen
import time
import snake
from food import Food
from scoreboard import Scoreboard
from power_ups import AddTwo

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

Game_Speed= 0.1
Slow_Down_Speed = 0.2


snake = snake.SnakeFunctions()
food = Food()
scoreboard = Scoreboard()
add_two = AddTwo()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(Game_Speed)
    snake.snake_move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        food.refresh()
        snake.extend()
        # Gets faster time every time you eat a piece of food.
        Game_Speed -= 0.001
    # Adds two extra segments if you catch the purple squares. Does not change score.
    if snake.head.distance(add_two) < 15:
        snake.extend()
        snake.extend()
        add_two.refresh()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False
    # Detect collision with tail using slicing to not count the head
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
