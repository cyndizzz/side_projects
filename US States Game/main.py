import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)
# get the coordinates from clicks
# def get_mouse_click_coords(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coords)
# turtle.mainloop()
is_game_on = True
guessed_state =[]

def add_state(state_name, x, y):
    tim = turtle.Turtle()
    tim.hideturtle()
    tim.color("black")
    tim.penup()
    tim.goto(x,y)
    tim.write(state_name, align='center', font=('Courier', 10, 'normal'))

data = pd.read_csv('50_states.csv')
all_states = data.state.tolist()
while len(guessed_state) < 50:
    answer_state = screen.textinput(title = f'{len(guessed_state)}/50 States Correct',
                                    prompt = "What is another state's name?").title()

    if answer_state in all_states:
        guessed_state.append(answer_state)
        state_data = data[data['state'] == answer_state]
        add_state(state_data.state.item(), state_data.x.item(), state_data.y.item())
    elif answer_state == 'Exit':
        missing_states = data[~data['state'].isin(guessed_state)]
        missing_states.to_csv('states_to_learn.csv', index=False)
        break
    else:
        print(1)

