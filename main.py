import time
from turtle import Screen
from car_manager import Car
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car = Car()
scoreboard = Scoreboard()
game_is_on = True
pace = 0


def crash():
    size = len(car.car_list) - 1
    for i in range(0, size):
        if car.car_list[i].distance(player) < 20:
            return True
    return False


while game_is_on:
    car.drive()
    if pace % 6 == 0:
        car.add_car()
    time.sleep(0.1)
    screen.update()
    pace += 1
    screen.onkey(player.move, "Up")
    screen.onkey(screen.bye, "q")
    if player.ycor() >= 200:
        scoreboard.count(1)
        scoreboard.broadcast()
        player.reset()
        time.sleep(0.2)
        car.increment += 10
    if crash():
        game_is_on = False

player.died()
screen.exitonclick()
