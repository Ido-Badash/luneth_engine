import json
from pathlib import Path
from typing import Dict


def dict_to_json_file(data: Dict, path: str):
    path: Path = Path(path)
    try:
        # make sure folder exists
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"JSON data successfully written to {path}")
    except IOError as e:
        print(f"Error writing to file {path}: {e}")


def dict_from_json_file(path: str) -> Dict:
    path = Path(path)
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"JSON data successfully extracted from {path}")
            return data
    except FileNotFoundError:
        print(f"File {path} not found.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {path}: {e}")
        return {}
    except IOError as e:
        print(f"Error reading the file {path}: {e}")
        return {}
