import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")

image = "Day 25 - US States Game/US States Game/blank_states_img.gif"

data = pandas.read_csv("Day 25 - US States Game/US States Game/50_states.csv")
all_states = data.state.to_list()

screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct", prompt= "What's another State's name ?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        
        new_data =  pandas.DataFrame(missing_states)
        new_data.to_csv("Day 25 - US States Game/US States Game/missed.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

############# Alternate code to find missed states ##################

# missed_states = list(set(all_states) - set(guessed_states))

# missed_states_data = pandas.DataFrame(missed_states)
# missed_states_data.to_csv("Day 25 - US States Game/US States Game/missed.csv")