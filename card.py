from enum import IntEnum


class Color(IntEnum): 
    RED = 0
    GREEN = 1
    PURPLE = 2

class Symbol(IntEnum):
    DIAMOND = 0
    SQUIGGLE = 1
    OVAL = 2

class Shading(IntEnum):
    SOLID = 0
    STRIPED = 1
    OPEN = 2

class Card: 
    pass 