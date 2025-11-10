from .core_types import ActionFunc, Trigger

DEFAULT_TRIGGER: Trigger = lambda: False
DEFAULT_ACTION: ActionFunc = lambda: None

DATA_FOLDER = "luneth_engine/data"
SETTINGS_FILE = DATA_FOLDER + "/settings.json"
