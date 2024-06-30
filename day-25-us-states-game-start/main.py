import turtle
from turtle import Screen, Turtle
import pandas as pd
FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



states_data = pd.read_csv("50_states.csv")
states_list = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Whats another state name?")
    user_answer = answer_state.title()
    missing_state = []
    if user_answer == "Exit":
        missing_state = [state for state in states_list if state not in guessed_states]
        # for state in states_list:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        # change missing state to csv
        data_new = pd.DataFrame(missing_state)
        data_new.to_csv("statestolearn.csv")
        break
    if user_answer in states_list:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        user_state_row = states_data[states_data.state == user_answer]
        t.goto(int(user_state_row.x), int(user_state_row.y))
        t.write(user_answer)




# print(states_list)
screen.exitonclick()