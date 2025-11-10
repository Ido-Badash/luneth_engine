from typing import List

from luneth_engine.utils.general_utils import next_in_lst, previous_in_lst

from .state import State


class StateManager:
    def __init__(self):
        self.states: List[State] = []
        self.state = None
        self.index = -1

    def add(self, state):
        self.states.append(state)
        if self.index == -1:
            self.index = 0
            self.state = state

    def remove(self, idx) -> State:
        removed = self.states.pop(idx)
        if idx == self.index:
            self.index = min(idx, len(self.states) - 1)
            self.state = self.states[self.index] if self.states else None
        elif idx < self.index:
            self.index -= 1
        return removed

    def state_idx(self, state) -> int:
        return self.states.index(state)

    def set_state(self, idx: int):
        self.index = idx
        self.state = self.states[idx]

    def next_state(self):
        self.state = next_in_lst(self.states, self.index)
        self.index = self.state_idx(self.state)

    def previous_state(self):
        self.state = previous_in_lst(self.states, self.index)
        self.index = self.state_idx(self.state)

    def finished_states(self) -> List:
        return [s for s in self.states if s.done]

    def unfinished_states(self) -> List:
        return [s for s in self.states if not s.done]
