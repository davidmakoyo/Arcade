def run_pong():
    from turtle import Screen
    from paddle import Paddle
    from ball import Ball
    import time
    from scoreboard import Scoreboard

    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("SuperPong")
    screen.tracer(0)

    paddle_1 = Paddle((350, 0))
    paddle_2 = Paddle((-350, 0))
    ball = Ball()
    score = Scoreboard()

    screen.listen()
    screen.onkey(paddle_1.up, "Up")
    screen.onkey(paddle_1.down, "Down")
    screen.onkey(paddle_2.up, "w")
    screen.onkey(paddle_2.down, "s")

    game_is_on = True
    while game_is_on:
        screen.update()
        ball.move()
        time.sleep(.01)

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()



        if ball.xcor() > 330 or ball.xcor() < -330:
            if ball.distance(paddle_2) < 50 or ball.distance(paddle_1) < 50:
                ball.speed()
                ball.hit()


        if ball.xcor() > 380:
            ball.set()
            ball.hit()
            score.l_point()



        if ball.xcor() < -380:
            ball.set()
            ball.hit()
            score.r_point()








    screen.exitonclick()

