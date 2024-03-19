from turtle import Turtle

FONT = ("Courier", 16, "normal")
FONT_Game_Over = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-220, 250)
        self.write(f"Level {self.level}: ", font=FONT, align="Center")

    def game_over(self):
        self.goto(0, 0)
        self.write("You Lose!", font=FONT_Game_Over, align="Center")

    def increase_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}: ", font=FONT, align="Center")
