import inspect
from typing import Any, Dict, Optional

from .constants import DEFAULT_ACTION, DEFAULT_TRIGGER
from .core_types import Action, ActionDict, ActionFunc, Trigger


class GlobalInputs:
    def __init__(self, actions: Optional[ActionDict] = None):
        self.actions: ActionDict = actions if actions else {}

    def add_action(
        self,
        name: str,
        trigger: Optional[Trigger] = DEFAULT_TRIGGER,
        action: Optional[ActionFunc] = DEFAULT_ACTION,
    ):
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

    def _safe_call(self, func, *args):
        """Call function safely, ignoring unexpected args errors"""
        try:
            return func(*args)
        except TypeError:
            try:
                return func()
            except Exception:
                return None

    def update(self, events=None, dt: Optional[float] = None):
        for a in self.actions.values():
            if self._safe_call(a["trigger"], events, dt):
                self._safe_call(a["action"], events, dt)
