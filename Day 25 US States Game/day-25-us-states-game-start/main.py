from turtle import Screen, shape, Turtle
import pandas as pd

# screen setup
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)

# Turtle setup
turtle = Turtle()
turtle.hideturtle()
turtle.up()

states_info = pd.read_csv("50_states.csv")
score = 0
correct_guessed_states = []

while (score<50):
    
    guess_state = screen.textinput(title=f"{score}/50 states Guessed", prompt="Guess the state name:").title()
    data = states_info[states_info["state"]==guess_state]

    if guess_state == "Exit":
        break
    elif len(data) == 1:
        x_coordinate = int(data["x"])
        y_coordinate = int(data["y"])
        turtle.goto(x_coordinate,y_coordinate)
        turtle.write(guess_state)
        correct_guessed_states.append(guess_state)
        score = score + 1

screen.mainloop()

# Creating the states_to_learn.csv
missing_states_dict = {"states":[state for state in states_info["state"] if state not in correct_guessed_states]}

missing_states = pd.DataFrame(missing_states_dict)
missing_states.to_csv("states_to_learn.csv")

# Showing the final result to the screen
print(f"Your Score: {score}\n")
print("All the guessed states:")
for index, state in enumerate(correct_guessed_states, start=1):
    print(f"{index}. {state}")