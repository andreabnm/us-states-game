import turtle
from game_engine import GameEngine

screen = turtle.Screen()
screen.title('U.S. States Quiz Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
engine = GameEngine()


while len(engine.states_guessed) < 50:
    answer_state = screen.textinput(title=f'{len(engine.states_guessed)}/{len(engine.all_states)} States Correct', prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        break
    engine.guess_state(answer_state)

engine.generate_to_learn_csv()