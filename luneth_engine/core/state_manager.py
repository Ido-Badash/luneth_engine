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
        # save old state
        old_state = self.state

        if old_state is not None:
            old_state.cleanup()

        res = func(self, *args, **kwargs)

        if self.state is not None:
            self.state.done = False
            self.state.startup()

        return res

    return wrapper


class StateManager:
    def __init__(self, states: Optional[List[State]] = None):
        self.states: List[State] = states or []
        self.index: int = 0 if self.states else -1
        self.state: Optional[State] = self.states[0] if self.states else None

    def add(self, state: State):
        """
        Add a new state to the manager.
        """
        self.states.append(state)
        if self.index == -1:
            self.index = 0
            self.state = state

    def remove(self, idx: int) -> State:
        """
        Remove a state by its index.
        Returns the removed state.
        """
        removed = self.states.pop(idx)
        if not self.states:
            # No states left
            self.state = None
            self.index = -1
        elif idx == self.index:
            # If removing current state, switch to closest
            self.index = min(idx, len(self.states) - 1)
            self.state = self.states[self.index]
        elif idx < self.index:
            # Adjust current index if needed
            self.index -= 1
        return removed

    @state_changed
    def set_state(self, idx: int):
        """
        Switch to a state by index.
        """
        if idx < 0 or idx >= len(self.states):
            raise IndexError("State index out of range")
        self.index = idx
        self.state = self.states[idx]

    def find_state_by_name(self, name: str) -> Optional[int]:
        """
        Return the index of a state by its name, or None if not found.
        """
        for i, s in enumerate(self.states):
            if s.name == name:
                return i
        return None

    def next_state(self):
        self.set_state(next_in_lst(self.states, self.index))

    def previous_state(self):
        self.set_state(previous_in_lst(self.states, self.index))
