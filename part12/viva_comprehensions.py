from typing import List, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    if parity == parity.ODD:
        result = [i for i in range(start, stop) if i % 2 != 0]
    elif parity == parity.EVEN:
        result = [i for i in range(start, stop) if i % 2 == 0]
    else:
        raise ValueError(f"Invalid parity option.")
    return result


def gen_dict(start: int, stop: int, strategy: Callable):
    return {i: strategy(i) for i in range(start, stop)}


def gen_set(val_in: str):
    return {c.upper() for c in set(val_in) if c.islower()}
