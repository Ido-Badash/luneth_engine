def cycle_lst(lst, current_idx: int, step: int) -> int:
    if not lst:
        return None
    return (current_idx + step) % len(lst)


def next_in_lst(lst, current_idx: int):
    return cycle_lst(lst, current_idx, 1)


def previous_in_lst(lst, current_idx: int):
    return cycle_lst(lst, current_idx, -1)


def key_from_val(d: dict, val):
    keys = list(d.keys())
    values = list(d.values())
    return keys[values.index(val)]


def cycle_dict(d: dict, current_val, step: int):
    keys = list(d.keys())
    current_idx = keys.index(current_val)
    key = cycle_lst(keys, current_idx, step)
    return d[key]


def next_in_dict(d: dict, current_val: int):
    return cycle_dict(d, current_val, 1)


def previous_in_dict(d: dict, current_val: int):
    return cycle_dict(d, current_val, -1)
