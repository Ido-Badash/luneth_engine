from typing import List, Optional, Callable

from luneth_engine.utils.general_utils import next_in_lst, previous_in_lst

from .state import State


def state_changed(func: Callable):
    """
    A decorator for function that change the current state

    cleanup current state -> declare it as done -> func() -> startup new state

    Wrapper returns the result from func()
    """

    def wrapper(self, *args, **kwargs):
        self.state.cleanup()
        self.state.done = True
        res = func(self, *args, **kwargs)
        self.state.startup()
        return res

    return wrapper


class StateManager:
    def __init__(self, states: Optional[List[State]] = None):
        self.states: List[State] = states if states else []
        self.state = None
        self.index = -1

        # init first state if states param was provided
        if self.states:
            self.index = 0
            self.state = self.states[0]

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

    @state_changed
    def set_state(self, idx: int):
        self.index = idx
        self.state = self.states[idx]

    @state_changed
    def next_state(self):
        self.state = next_in_lst(self.states, self.index)
        self.index = self.state_idx(self.state)

    @state_changed
    def previous_state(self):
        self.state = previous_in_lst(self.states, self.index)
        self.index = self.state_idx(self.state)

    def finished_states(self) -> List:
        return [s for s in self.states if s.done]

    def unfinished_states(self) -> List:
        return [s for s in self.states if not s.done]

    def find_state_by_name(self, name: str):
        for i, state in enumerate(self.states):
            if state.name == name:
                return i
        return None

    def default_switcher(self):
        """Default state switcher, used in the bottom of a While loop\n
        Returns `False` if didnt find a state"""
        next_state_name = self.state.next
        self.state.done = False  # reset
        self.state.next = None  # clear

        # find and switch to the named state
        state_idx = self.find_state_by_name(next_state_name)
        if state_idx is not None:
            self.set_state(state_idx)
            return True
        else:
            print(f"Warning: State '{next_state_name}' not found")
            self.state = None  # clear current state
            return False  # no matching state found
