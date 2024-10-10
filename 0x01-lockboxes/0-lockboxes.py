#!/usr/bin/python3

"""
Function to unlock boxes
"""


def canUnlockAll(boxes):
    """
    Determines the boxes that are unlocked
    Sets the first box unlocked and the keys
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    
    for box in range(1, len(boxes)):
        can_open = False
        
        for idx in range(len(boxes)):
            if box in boxes[idx] and box != idx:
                can_open = True
                break
            
        if not can_open:
            return False