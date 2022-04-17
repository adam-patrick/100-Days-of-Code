from player import Player
from turtle import Turtle
FONT = ("Courier", 24, "normal")
player = Player()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-200, 200)
        self.write(self.level, align="left", font=FONT)

    def next_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)