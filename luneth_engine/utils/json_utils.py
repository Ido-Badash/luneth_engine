import json
from pathlib import Path
from typing import Dict
from .general_utils import resource_path


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
    print(f"[DEBUG] Original path: {path}")
    resolved_path = resource_path(path)
    print(f"[DEBUG] Resolved path: {resolved_path}")

    path = Path(resolved_path)
    print(f"[DEBUG] Path object: {path}")
    print(f"[DEBUG] Path exists: {path.exists()}")

    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"JSON data successfully extracted from {path}")
            print(f"[DEBUG] Keys in data: {list(data.keys())}")
            return data
    except FileNotFoundError:
        print(f"[ERROR] File {path} not found.")
        return {}
    except json.JSONDecodeError as e:
        print(f"[ERROR] Error decoding JSON from {path}: {e}")
        return {}
    except IOError as e:
        print(f"[ERROR] Error reading the file {path}: {e}")
        return {}
