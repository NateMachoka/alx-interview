#!/usr/bin/python3
"""
Function determines whether all the boxes in a list of lists can be unlocked.
Each box contains keys to other boxes. You start with the first box unlocked and
must find keys to unlock all other boxes.

The function returns True if all boxes can be unlocked, else it returns False.
"""

def canUnlockAll(boxes):
    """
    Args:
    boxes (list of lists): Each inner list represents a box

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]


    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    # Return True if all boxes are unlocked, False otherwise
    return all(unlocked)
