from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle_Crossing_Game")
screen.setup(width=600,height=600)
screen.tracer(0) # Turn of the animation on the screen

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move,"Up")



game_is_on= True
while game_is_on:
    time.sleep(0.1) # after 0.1 ms screen update takes place
    screen.update() # Manually update the screen

    car_manager.create_car()
    car_manager.move_car()
    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when the player has reached the finished line
    if player.is_on_finished_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.inc_level()










screen.exitonclick()