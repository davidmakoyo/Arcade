from turtle import Screen
from snake import Snake
import time
from food import Food
from snakescore import Scoreboard

def run_snake():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()

            scoreboard.update()
            snake.extend()

        if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
            snake.reset()
            food.reset()
            game_is_on = False



        for segment in snake.segments:
            if segment == snake.head:
                pass

            elif snake.head.distance(segment) < 10:
                snake.reset()
                food.reset()
                game_is_on = False






    screen.exitonclick()