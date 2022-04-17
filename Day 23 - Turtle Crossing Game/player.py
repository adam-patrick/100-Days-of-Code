from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)
        self.is_level_done = False

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() == 300:
            self.is_level_done = True
        else:
            self.is_level_done = False

    def run_home_jack(self):
        self.goto(0, -280)
        self.is_level_done = False
