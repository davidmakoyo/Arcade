def guesser():
    import turtle
    import pandas
    from turtle import Turtle

    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    cursor = Turtle()
    cursor.penup()
    cursor.hideturtle()

    number_correct = 0
    data = pandas.read_csv("50_states.csv")
    state_list = data.state.str.strip().tolist()
    correct_guesses = []
    data = pandas.read_csv("50_states.csv")


    while number_correct < 50:
        answer_state = (screen.textinput(title=f"{number_correct}/50 Correct", prompt="Enter a state")).strip().title()
        if answer_state == "Exit":
            missing_states = [state for state in state_list]
            missed_states = pandas.DataFrame(missing_states)
            missed_states.to_csv("missed_states.csv")
            break

        if answer_state in state_list:
            correct_guesses.append(answer_state)
            number_correct += 1
            state_list.remove(answer_state)
            state_row = data[data.state.str.strip() == answer_state]
            state_x = state_row.x.values[0]
            state_y = state_row.y.values[0]
            cursor.goto(state_x, state_y)
            cursor.write(answer_state)












