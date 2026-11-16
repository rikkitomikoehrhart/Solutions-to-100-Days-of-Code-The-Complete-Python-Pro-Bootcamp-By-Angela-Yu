import turtle as t_mod
import pandas

IMAGE = "blank_states_img.gif"

screen = t_mod.Screen()
screen.title("U.S. Game")
screen.setup(width=725, height=491)
screen.setworldcoordinates(llx=-362.5, lly=-245.5, urx=362.5, ury=245.5)
screen.bgpic(IMAGE)
screen.addshape(IMAGE)
t_mod.shape(IMAGE)

guessed_states = []

data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States", prompt="Name a missing state: ").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        label = t_mod.Turtle()
        label.hideturtle()
        label.penup()
        state_data = data[data.state == answer_state]
        label.goto(state_data.x.item(), state_data.y.item())
        label.write(answer_state)





screen.exitonclick()