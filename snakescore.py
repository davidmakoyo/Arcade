from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(-250, 280)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.write(arg=f"Score: {self.score}", font=('Arial', 12, 'bold'), align="center")

    def update(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", font=('Arial', 12, 'bold'), align="center")