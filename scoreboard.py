from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.value = 1
        self.pencolor("black")
        self.hideturtle()
        self.broadcast()

    def count(self, num):
        self.value = self.value + num

    def broadcast(self):
        self.clear()
        self.penup()
        message = f"Level:{self.value}"
        self.setposition(-260, 260)
        self.pendown()
        self.write(message, font=("Courier", 24, "normal"))
