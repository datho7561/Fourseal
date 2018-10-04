from enum import Enum

class Direction(Enum):
    """ Used to describe which direction an entity is facing and travelling """

    UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT = list(range(8))


def perpendicular(direction):
    """ Returns a tuple of the two directions perpendicular to this one """

    # FIXME: Wizardry that will breaks if I decide
    #        to add more directions to the Enum
    return (Direction((direction.value + 2) % 8),
                Direction((direction.value + 2) % 8))


def opposite(direction):
    """ Returns the direction opposite this one """
    # FIXME: More wizardry
    return Direction((direction.value + 4) % 8)


def dirsAsArray():
    return (Direction.UP, Direction.UP_RIGHT, Direction.RIGHT,
           Direction.DOWN_RIGHT, Direction.DOWN,
           Direction.DOWN_LEFT, Direction.LEFT,
           Direction.UP_LEFT)