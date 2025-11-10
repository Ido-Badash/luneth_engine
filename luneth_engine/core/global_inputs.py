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
        trigger = trigger or old.get("trigger", DEFAULT_TRIGGER)
        action = action or old.get("action", DEFAULT_ACTION)
        self.actions[name] = {"trigger": trigger, "action": action}

    def _smart_call(self, func, events=None, dt=None):
        """Call func() based on its signature"""
        try:
            sig = inspect.signature(func)
            params = list(sig.parameters.keys())

            # match by parameter names
            if len(params) == 0:
                return func()
            elif len(params) == 1:
                if "events" in params:
                    return func(events)
                elif "dt" in params:
                    return func(dt)
                else:
                    return func()  # unknown param name, fallback
            elif len(params) >= 2:
                return func(events, dt)
        except Exception:
            return None

    def update(self, events=None, dt=None):
        """Update all actions"""
        for a in self.actions.values():
            if self._smart_call(a["trigger"], events, dt):
                self._smart_call(a["action"], events, dt)
