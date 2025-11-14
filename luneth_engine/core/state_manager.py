from typing import List, Optional, Callable

from luneth_engine.utils.general_utils import next_in_lst, previous_in_lst
from .state import State


def state_changed(func: Callable):
    def wrapper(self, *args, **kwargs):
        old_state = self.state

        if old_state is not None:
            old_state.cleanup()

        res = func(self, *args, **kwargs)

        new_state = self.state

        if old_state != new_state and self.on_state_change is not None:
            self.on_state_change(old_state, new_state)

        if new_state is not None:
            new_state.startup()

        return res

    return wrapper


ON_STATE_CHANGE_TYPE = Callable[[Optional[State], Optional[State]], None]


class StateManager:
    def __init__(
        self,
        states: Optional[List[State]] = None,
        on_state_change: Optional[ON_STATE_CHANGE_TYPE] = None,
    ):
        self.states: List[State] = states or []
        self.state: Optional[State] = self.states[0] if states else None
        self.on_state_change = on_state_change

    # --- index handling ---
    @property
    def index(self) -> int:
        if self.state is None:
            return -1
        return self.states.index(self.state)

    @index.setter
    def index(self, val: int):
        if 0 <= val < len(self.states):
            self.state = self.states[val]
        else:
            self.state = None

    # --- state list management ---
    def add(self, state: State):
        self.states.append(state)
        if self.state is None:
            self.state = state

    def remove(self, idx: int) -> State:
        removed = self.states.pop(idx)

        if not self.states:
            self.state = None
            return removed

        # if removed current → move to closest
        if idx == self.index:
            self.index = min(idx, len(self.states) - 1)

        # if removed before current → shift left
        elif idx < self.index:
            self.index -= 1

        return removed

    # --- switching ---
    @state_changed
    def set_state(self, name: str):
        idx = self.find_state_by_name(name)
        if idx is None:
            print(f'[WARNING] No state named "{name}"')
            return False
        self.state = self.states[idx]
        return True

    def find_state_by_name(self, name: str) -> Optional[int]:
        for i, s in enumerate(self.states):
            if s.name == name:
                return i
        return None

    # --- next & previous ---
    def next_state(self):
        if self.state:
            idx = next_in_lst(self.states, self.index)
            self.set_state(self.states[idx].name)

    def previous_state(self):
        if self.state:
            idx = previous_in_lst(self.states, self.index)
            self.set_state(self.states[idx].name)
