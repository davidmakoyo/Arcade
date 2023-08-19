from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.seth(90)
        self.setpos(0, -280)
        self.color("black")
        self.shape("turtle")

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)


