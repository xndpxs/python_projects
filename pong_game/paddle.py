from turtle import Turtle

WIDTH = 20
HEIGHT = 100
STR_WIDTH = 5
STR_LENGTH = 1


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=STR_WIDTH, stretch_len=STR_LENGTH)

    def set_position(self, position):
        self.penup()
        self.goto(position, 0)

    def go_up(self):
        up_y = self.ycor() + 20
        self.goto(self.xcor(), up_y)

    def go_down(self):
        down_y = self.ycor() - 20
        self.goto(self.xcor(), down_y)
