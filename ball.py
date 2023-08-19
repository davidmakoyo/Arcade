from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 1
        self.y_move = 1


    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)


    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1

    def set(self):
        self.setpos(0,0)
        self.x_move = 1
        self.y_move = 1

    def speed(self):
        self.x_move *= 1.25
        self.y_move *= 1.25