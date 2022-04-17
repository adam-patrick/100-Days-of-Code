import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FONT = ("Courier", 24, "normal")

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

# Turtle will only go forward
screen.listen()
screen.onkey(player.move_up, "Up")

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.cars()
    car_manager.move_cars()

# Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    scoreboard.display_score()
# Determine whether the level is beaten or not
    player.finish_line()
    if player.is_level_done:
        scoreboard.next_level()
        player.run_home_jack()
        car_manager.next_level_speed()
    if not game_is_on:
        scoreboard.game_over()

screen.exitonclick()
