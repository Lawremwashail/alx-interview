#!/usr/bin/python3
"""
Module to unlock a series of locked boxes using available keys.
"""


def canUnlockAll(boxes):
    """
    Determines whether all the boxes can be unlocked.
    
    Args:
    boxes (list of lists): A list where each element is a list of keys for other boxes.
    
    Returns:
    bool: True if all boxes can be opened, else False.
    """
    if not isinstance(boxes, list):
        return False

    if len(boxes) == 0:
        return False

    for box in range(1, len(boxes)):
        can_open = False
        for idx in range(len(boxes)):
            if box in boxes[idx] and box != idx:
                can_open = True
                break
        if not can_open:
            return False
    return True
