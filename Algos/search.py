from typing import List, Optional
import logging


def binary_search(list_in: List[int], item: int) -> Optional[int]:
    """
    If item exists in list_in, this function returns its position in the list.
    """
    low_pos = 0  # lowest position 
    high_pos = len(list_in) - 1  # highest position

    while low_pos <= high_pos:
        mid_pos = (low_pos + high_pos) // 2  # middle position for contenders
        guess = list_in[mid_pos]  # value for middle position

        logging.info(f"low: {low_pos} high: {high_pos}. guess: {guess}")

        if guess == item:
            return mid_pos
        elif guess > item:
            high_pos = mid_pos
        else:
            low_pos = mid_pos + 1

    return None
