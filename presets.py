""" presets.py

holds some constants for the common conway creations
"""

GLIDER = [
    (1,3),
    (2,4),
    (3,2),
    (3,3),
    (3,4)
]

BLINKER = [
    (1,1),
    (1,2),
    (2,1),
    (2,2),
    (3,3),
    (3,4),
    (4,3),
    (4,4)
]

SQUARE = [
    (1,1),
    (1,2),
    (2,1),
    (2,2)
]

ALL = [GLIDER, BLINKER, SQUARE]  # for iterating in a menu