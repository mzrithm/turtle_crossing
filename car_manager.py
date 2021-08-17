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
        self.setposition(260, randint(-300, 300))
        self.shape("square")
        self.color(colors[randint(0, 5)])
        self.turtlesize(stretch_wid=1, stretch_len=2)
        print(self.position())
        # self.showturtle()
        self.car_list = []
        self.speed = 1
        self.go = 0

    def create_cars(self):
        new_car = Car()
        self.car_list.append(new_car)

    def drive(self):
        size = len(self.car_list) - 1
        self.car_list[self.go].showturtle()
        self.car_list[self.go].backward(5)
        if size == 1:
            self.go += 1
            if self.car_list[self.go - 1].xcor() < 240:
                self.car_list[self.go].showturtle()
                self.car_list[self.go].backward(5)
        # if size >= 2:
        #     start += 1
        #     if self.car_list[start - 1].xcor() < 240:
        #         self.car_list[start].showturtle()
        #         self.car_list[start].backward(5)
        pass
    #     num = len(self.car_list) - 1
    #     print(num)
    #     if num == 0:
    #         new_x = self.xcor() - 5
    #         self.setposition(new_x, self.ycor())
    #     else:
    #         for i in range(0, num):
    #             new_x = self.car_list[num].xcor() - 5
    #             self.car_list[num].setposition(new_x, self.car_list[num].ycor())
    #             print(num, self.car_list[num].position())
    #             # self.car_list[num].backward(5)
    #             if self.car_list[num].xcor() == -300:
    #                 self.car_list[num].hideturtle()
