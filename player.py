from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setposition(0, -200)
        self.setheading(90)
        self.increment = 10

    def move(self):
        self.forward(self.increment)

    def reset(self):
        self.setposition(0, -200)

    def died(self):
        ending = Turtle()
        ending.hideturtle()
        ending.color("black")
        ending.write("GAME OVER", align="center", font=("Arial", 30, "bold"))



