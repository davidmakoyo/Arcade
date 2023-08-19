def cross():
    import time
    from turtle import Screen
    from player import Player
    from player import STARTING_POSITION
    from car_manager import CarManager
    from turtlescore import Scoreboard

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.up, "Up")

    counter = 0
    game_is_on = True

    while game_is_on:
        time.sleep(0.1)
        screen.update()
        counter += 1

        if player.ycor() >= 280:
            player.setpos(STARTING_POSITION)
            car_manager.level_up()
            car_manager.speed_up_all()
            scoreboard.point()

        if counter % 3 == 0:
            car = CarManager()

        for car in CarManager.instances:
            if player.distance(car) < 15:
                game_is_on = False

        car_manager.move_all()


