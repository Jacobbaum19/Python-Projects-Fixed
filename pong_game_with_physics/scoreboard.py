from turtle import Turtle

"""This code contains the logic for the scoreboard."""

ALIGN = "center"
FONT = ("Times New Roman", 50, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.clear()  # Clear the previous score
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def write_winner(self):
        if self.l_score == 10:
            self.goto(0, 0)
            self.write("Left Player Wins!", align=ALIGN, font=FONT)
        else:
            self.goto(0, 0)
            self.write("Right Player Wins!", align=ALIGN, font=FONT)
