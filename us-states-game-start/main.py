import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
score = 0
correct_guesses = []


while len(correct_guesses) < 50:
    answer_state = (screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?")).title()
    if answer_state == "Exit":
        states_to_learn = []
        for state in states_list:
            if state not in correct_guesses:
                states_to_learn.append(state)

        new_data = pandas.Series(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        score += 1
        state = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state.x), int(state.y))
        t.write(answer_state)

    else:
        answer_state = (screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?")).title()
