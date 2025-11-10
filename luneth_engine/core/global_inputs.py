import inspect
from typing import Any, Dict, Optional

from .constants import DEFAULT_ACTION, DEFAULT_TRIGGER
from .core_types import Action, ActionDict, ActionFunc, Trigger


class GlobalInputs:
    def __init__(self, actions: Optional[ActionDict] = None):
        self.actions: ActionDict = actions if actions else {}

    def add_action(self, name: str, trigger: Trigger, action: ActionFunc):
        self.actions[name] = {"trigger": trigger, "action": action}

    def get_action(
        self, name: str, default: Optional[Action] = None
    ) -> Optional[Action]:
        return self.actions.get(name, default)

    def set_action(
        self,
        name: str,
        trigger: Optional[Trigger] = DEFAULT_TRIGGER,
        action: Optional[ActionFunc] = DEFAULT_ACTION,
    ):
        old = self.actions.get(name, {})
        trigger = trigger if trigger else old.get("trigger", DEFAULT_TRIGGER)
        action = action if action else old.get("action", DEFAULT_ACTION)
        self.actions[name] = {"trigger": trigger, "action": action}

    def update(self, events=None, dt: Optional[float] = None):
        """Call this every frame (events and dt optional)."""
        for action in self.actions.values():
            if self._safe_call(action["trigger"], events, dt):
                self._safe_call(action["action"], events, dt)

    def _safe_call(func, *args):
        """Call a function with args only if it expects them"""
        try:
            sig = inspect.signature(func)
            if len(sig.parameters) == 0:
                return func()
            elif len(sig.parameters) == 1:
                return func(args[0])
            else:
                return func(*args)
        except Exception:
            return None
