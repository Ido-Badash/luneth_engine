from typing import Callable, Dict, TypedDict

Trigger = Callable[[], bool]  # a function that returns True if action should run
ActionFunc = Callable[[], None]  # a function that performs the action


class Action(TypedDict):
    trigger: Trigger
    action: ActionFunc


ActionDict = Dict[str, Action]
