import time
from turtle import Screen
from car_manager import Car
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = Car()
game_is_on = True

while game_is_on:
    car.create_cars()
    car.drive()
    time.sleep(0.1)

    time.sleep(0.1)
    screen.update()
