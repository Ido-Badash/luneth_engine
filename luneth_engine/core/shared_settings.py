from typing import Any, Optional


class SharedSettings:
    def __init__(self):
        self.settings = {}

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
        # Will save current settings into a json file
        # Not needed for now
        pass

    def load(self):
        # Loads the json file and replaces self.settings
        # Not needed for now
        pass
