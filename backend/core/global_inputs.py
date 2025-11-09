from typing import Any, Dict, Optional

from constants import DEFAULT_ACTION, DEFAULT_TRIGGER
from core_types import Action, ActionDict, ActionFunc, Trigger


class GlobalInputs:
    def __init__(self, settings: Dict[str, Any], actions: Optional[ActionDict] = None):
        self.settings: Dict[str, Any] = settings
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

    def update(self):
        """Call this every frame with events"""
        for action in self.actions.values():
            if action["trigger"]():
                action["action"]()
