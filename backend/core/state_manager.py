from utils.general_utils import next_in_lst, previous_in_lst

from .state import State


class StateManager:
    def __init__(self):
        self.states = []
        self.current_state = None

    def add(self, state):
        self.states.append(state)

    def remove(self, idx):
        self.states.pop(idx)

    def state_idx(self, state):
        return self.states.index(state)

    def set_state(self, idx: int):
        self.current_state = self.states[idx]

    def next_state(self):
        self.current_state = next_in_lst(
            self.states, self.states.index(self.current_state)
        )

    def previous_state(self):
        self.current_state = previous_in_lst(
            self.states, self.states.index(self.current_state)
        )
