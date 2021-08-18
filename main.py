import time
from turtle import Screen
from car_manager import Car
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = Car()
car_place = 260
game_is_on = True
pace = 0

while game_is_on:
    car.drive()
    if pace % 6 == 0:
        car.add_car()
    time.sleep(0.1)
    screen.update()
    pace += 1

