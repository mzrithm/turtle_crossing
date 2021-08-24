from turtle import Turtle
from random import randint

colors = ["red", "orange", "green", "blue", "yellow", "purple"]


class Car(Turtle):
    """Generate random selection of car objects
    moving at set speed along y-axis.
    """

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.car_list = []
        self.speed = 1
        self.increment = 5

    def add_car(self):
        new_car = Turtle("square")
        new_car.hideturtle()
        new_car.penup()
        new_car.speed(1)
        new_car.color(colors[randint(0, 5)])
        new_car.turtlesize(stretch_wid=1, stretch_len=2)
        new_car.setposition(315, randint(-160, 200))
        new_car.showturtle()
        self.car_list.append(new_car)

    def drive(self):
        size = len(self.car_list) - 1
        for i in range(0, size):
            self.car_list[i].backward(self.increment)
