from turtle import Turtle
import time
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    instances = []
    current_speed = STARTING_MOVE_DISTANCE
    def __init__(self):
        super().__init__()
        CarManager.instances.append(self)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.setpos(280, random.randint(-280,280))
        self.color(random.choice(COLORS))
        self.move_distance = CarManager.current_speed


    def move(self):
            self.goto(self.xcor() - self.move_distance, self.ycor())

    def level_up(self):
        CarManager.current_speed += MOVE_INCREMENT

    def move_all(cls):
        for instance in cls.instances:
            instance.move()

    def speed_up_all(cls):
        for instance in cls.instances:
            instance.move_distance = CarManager.current_speed



