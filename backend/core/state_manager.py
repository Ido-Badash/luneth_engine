from typing import List

from state import State

from utils.general_utils import next_in_lst, previous_in_lst


class StateManager:
    def __init__(self):
        self.states: List[State] = []
        self.current_state = None
        self.current_idx = -1

    def add(self, state):
        self.states.append(state)
        if self.current_idx == -1:
            self.current_idx = 0
            self.current_state = state

    def remove(self, idx) -> State:
        removed = self.states.pop(idx)
        if idx == self.current_idx:
            self.current_idx = min(idx, len(self.states) - 1)
            self.current_state = self.states[self.current_idx] if self.states else None
        elif idx < self.current_idx:
            self.current_idx -= 1
        return removed

    def state_idx(self, state) -> int:
        return self.states.index(state)

    def set_state(self, idx: int):
        self.current_idx = idx
        self.current_state = self.states[idx]

    def next_state(self):
        self.current_state = next_in_lst(self.states, self.current_idx)
        self.current_idx = self.state_idx(self.current_state)

    def previous_state(self):
        self.current_state = previous_in_lst(self.states, self.current_idx)
        self.current_idx = self.state_idx(self.current_state)

    def finished_states(self) -> List:
        return [s for s in self.states if s.done]

    def unfinished_states(self) -> List:
        return [s for s in self.states if not s.done]
