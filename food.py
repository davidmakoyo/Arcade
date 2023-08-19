from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("cyan")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def reset(self):
        self.goto(1000,1000)