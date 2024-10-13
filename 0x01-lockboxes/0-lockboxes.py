#!/usr/bin/python3

""" Python module that determines if all
boxes can be opened/unblockedfrom a list
of lists! Prototype:def canUnlockAll(boxes)"""


def canUnlockAll(boxes=[]):
    """Function that returns True if all box in
    boxes can be opend or else returns False"""
    if not boxes:
        return False

    keys = set([0])
    for box_id, box in enumerate(boxes):
        for key in box:
            if key < len(boxes) and key != box_id:
                keys.add(key)

    if len(keys) != len(boxes):
        return False

    return True


if __name__ == '__main__':
    boxes = [
                [1, 3],
                [2],
                [3, 0],
                [1, 2, 3],
            ]
    print(unlockBoxes(boxes))

    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(unlockBoxes(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(unlockBoxes(boxes))
