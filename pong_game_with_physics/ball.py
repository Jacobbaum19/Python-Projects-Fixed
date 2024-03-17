from turtle import Turtle

"""This code contains mostly the ball logic and grabs the l and r paddles from the main file.
I tried adding spin to the game to make it more interesting but can't quite figure it out yet"""

# Starting speeds
X_Speed = 0.16
Y_Speed = 0.16


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.scoreboard = None
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.setposition(position)
        self.x_move = X_Speed
        self.y_move = Y_Speed
        # Making empty paddles
        self.l_paddle = None
        self.r_paddle = None
        self.spin = 0

    # Taking paddles from main

    def set_paddles(self, l_paddle, r_paddle):
        self.l_paddle = l_paddle
        self.r_paddle = r_paddle

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move + self.spin
        self.goto(new_x, new_y)

        # Simulate friction by decreasing the spin as it is moving
        self.spin *= 0.555

    def reset_ball_l(self):
        self.goto(0, 0)
        self.x_move = -abs(X_Speed)  # Ensures the ball moves left
        self.spin = 0
        self.move()  # Use a generic move method that handles both x and y movement

    def reset_ball_r(self):
        self.goto(0, 0)
        self.x_move = abs(X_Speed)  # Ensures the ball moves right
        self.spin = 0
        self.move()  # Use a generic move method that handles both x and y movement

    def ball_bonce_wall(self):
        if self.ycor() > 285 or self.ycor() < -285:
            self.y_move *= -1

    def ball_bonce_paddle(self):
        if self.distance(self.r_paddle) < 50 and self.xcor() > 320:  # Collision with right paddle
            self.x_move *= -1  # Reverse x-direction
            # Calculate difference in y position between ball and paddle
            y_diff = self.ycor() - self.r_paddle.ycor()
            # Add spin to the ball
            self.spin = y_diff * 0.05  # start with 0.05
            # Adjust y_move based on y_diff
            self.y_move = y_diff * 0.01  # Seems like 0.01 is the best to use without breaking the game...

        elif self.distance(self.l_paddle) < 50 and self.xcor() < -315:  # Collision with left paddle
            self.x_move *= -1  # Reverse x-direction
            # Calculate difference in y position between ball and paddle
            y_diff = self.ycor() - self.l_paddle.ycor()
            # Add spin to the ball
            self.spin = y_diff * 0.05  # start with 0.05
            # Adjust y_move based on y_diff
            self.y_move = y_diff * 0.01

    # Logic to be able to use the scoreboard class inside the ball functions
    def set_scoreboard(self, scoreboard):
        self.scoreboard = scoreboard

    def ball_misses(self):
        if self.xcor() > 400:
            self.reset_ball_l()
            print("Right missed!")
            self.scoreboard.l_point()  # Left scores
        elif self.xcor() < -400:
            self.reset_ball_r()
            print("Left Missed!")
            self.scoreboard.r_point()  # Right scores
