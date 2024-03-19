from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):
    """Taking the same instances of car_manager and the scoreboard so nothing funky happens and
    # there is no chance that one data does not match the other data."""
    def __init__(self, car_manager, scoreboard):
        super().__init__()
        self.car_manager = car_manager
        self.scoreboard = scoreboard
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        """Resets the player back to the starting position, clears cars, increases their speed and spawn rate
        Adds +1 to the level"""
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.car_manager.clear_cars()
            self.car_manager.increase_speed()
            self.car_manager.increase_spawn_rate()
            self.scoreboard.increase_score()

    def player_get_hit(self):
        """Player collision with a car is detected from the car.manager list and sends it back to main.py"""
        for car in self.car_manager.cars:
            if self.distance(car) < 25:
                return True
        return False
