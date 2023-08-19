from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.starting_positions = [(0,0), (-20, 0), (-40, 0)]
        self.segments = []
        for position in self.starting_positions:
            self.add_segment(position)
        self.head = self.segments[0]
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(new_pos)
        self.segments[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].seth(UP)
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].seth(DOWN)
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].seth(RIGHT)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].seth(LEFT)
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(self.segments[-1].pos())
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)

