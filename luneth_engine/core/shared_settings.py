from pathlib import Path
from typing import Any, Dict, Optional

from luneth_engine.utils.json_utils import dict_from_json_file, dict_to_json_file

from .constants import SETTINGS_FILE


class SharedSettings:
    def __init__(
        self, config: Optional[Dict[str, Any]] = None, json_path: Optional[str] = None
    ):
        self.settings = config if config else {}
        self.path = Path(json_path) if json_path else Path(SETTINGS_FILE)

    def add(self, setting_name: str, value: Any = None):
        if setting_name in self.settings:
            raise KeyError(f"Setting '{setting_name}' already exists")
        self.settings[setting_name] = value

    def remove(self, setting_name: str, default: Any = None):
        return self.settings.pop(setting_name, default)

    def update(self, new_settings: Dict[str, Any]):
        self.settings.update(new_settings)

    def get(self, setting_name: str, default: Any = None):
        return self.settings.get(setting_name, default)

    def set(self, setting_name: str, new_value: Any = None):
        self.settings[setting_name] = new_value

    def keys(self):
        return self.settings.keys()

    def items(self):
        return self.settings.items()

    def sadd(self, setting_name: str, value: Any = None):
        "Like the `add` method but also uses the `save` method right after"
        self.add(setting_name, value)
        self.save()

    def sremove(self, setting_name: str, default: Any = None):
        "Like the `remove` method but also uses the `save` method right after"
        self.remove(setting_name, default)
        self.save()

    def supdate(self, new_settings: Dict[str, Any]):
        "Like the `update` method but also uses the `save` method right after"
        self.settings.update(new_settings)
        self.save()

    def lget(self, setting_name: str, default: Any = None):
        "Like the `get` method but also uses the `load` method right before"
        self.load()
        return self.get(setting_name, default)

    def sset(self, setting_name: str, new_value: Any = None):
        "Like the `set` method but also uses the `save` method right after"
        self.set(setting_name, new_value)
        self.save()

    def save(self):
        """Saves to json current settings"""
        self.path.parent.mkdir(parents=True, exist_ok=True)  # make sure folder exists
        dict_to_json_file(self.settings, str(self.path))

    def load(self):
        """Getting the setting from the json and sets them as current settings"""
        if self.path.exists():
            self.settings = dict_from_json_file(str(self.path))
