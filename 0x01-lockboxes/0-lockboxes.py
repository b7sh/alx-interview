#!/usr/bin/python3
"""
- Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    Arguments:
    boxes --> List of Lists, it contains the boxes with keys
    Variables:
    myKeys --> List, Store the keys to open boxes
    key --> integer, key of myKeys
    boxKey --> integer, key inside of an specific box
    box_length --> integer, length of the box
    """
    box_length = len(boxes)
    myKeys = [0]
    for key in myKeys:
        for boxKey in boxes[key]:
            if boxKey not in myKeys and boxKey < box_length:
                myKeys.append(boxKey)
    if len(myKeys) == box_length:
        return True
    return False
