#!/usr/bin/python3

"""
Function to unlock boxes
"""


def canUnlockAll(boxes):
    """
    Determines the boxes that are unlocked
    Sets the first box unlocked and the keys
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    
    for box in range(1, len(boxes) - 1):
        can_open = False
        
        for idx in range(len(boxes)):
            can_open = box in boxes[idx] and box != idx
            
            if can_open:
                break
            
        if can_open is False:
            return can_open
        
    return True
