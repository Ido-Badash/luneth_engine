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
        self.settings[setting_name] = value

    def get(self, setting_name: str, default: Any = None):
        return self.settings.get(setting_name, default)

    def set(self, setting_name: str, new_value: Any = None):
        self.settings[setting_name] = new_value

    def keys(self):
        return self.settings.keys()

    def items(self):
        return self.settings.items()

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)  # make sure folder exists
        dict_to_json_file(self.settings, self.path)

    def load(self):
        if self.path.exists():
            self.settings = dict_from_json_file(self.path)
