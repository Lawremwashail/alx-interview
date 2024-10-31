#!/usr/bin/python3
"""
UTF-8 Validation
"""


def get_leading_bits(num):
    """
    Returns the number of leading set bits (1) in a byte
    """
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    num_bytes = 0
    for byte in range(len(data)):
        if num_bytes == 0:
            num_bytes = get_leading_bits(data[byte])
        if num_bytes == 0:
            continue

            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (data[byte] & (1 << 7) and not (data[byte] & (1 << 6))):
                return False

        num_bytes -= 1

    return num_bytes == 0
