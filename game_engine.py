from turtle import Turtle
import pandas

DATA_FILE = '50_states.csv'


class GameEngine(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.data = pandas.read_csv(DATA_FILE)
        self.all_states = self.data['state'].tolist()
        self.states_guessed = []

    def guess_state(self, state):
        if (state in self.all_states) and not (state in self.states_guessed):
            self.place_on_map(state)
            self.states_guessed.append(state)
            return True

    def place_on_map(self, state):
        state_row = self.data[self.data['state'] == state]
        self.goto(int(state_row['x'].iloc[0]), int(state_row['y'].iloc[0]))
        self.write(state, align='center')

    def generate_to_learn_csv(self):
        states_to_learn = list(set(self.all_states) - set(self.states_guessed))
        if states_to_learn:
            pandas.DataFrame(states_to_learn).to_csv('states_to_learn.csv')


