import turtle
import pandas




screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_state=[]

while len(guessed_state)<50:
    answer_state=screen.textinput(title=f"{len(guessed_state)}/50 states",prompt="what's another state name?").title()
    if answer_state=="Done":
        missed_state=[state for state in all_states if state not in guessed_state]
        # for state in all_states:
        #     if state not in guessed_state:
        #         missed_state.append(state)
        missed_dict=pandas.DataFrame(missed_state)
        missed_dict.to_csv("to be learn")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        st=turtle.Turtle()
        st.hideturtle()
        st.penup()
        state_data=data[data.state==answer_state]
        st.goto(int(state_data.x),int(state_data.y))
        st.write(answer_state)
