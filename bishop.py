# Author: David Thompson
# Date: 3 October, 2018
# Purpose: Like the Pawn, except it goes after the player, goes faster, and hits stronger

from constants import *
from entity import Entity
from sprite import Sprite
from direction import Direction
from direction import perpendicular, opposite, dirsAsArray
from foe import Foe
from player import Player
import random


class Bishop(Foe):

    def __init__(self, images, xpos = 0, ypos = 0, maxHealth = 80,
                resistance = 0, damage = 30, range = 5, speed = 1.2,
                attackSpeed = 45, direction = None):
        # Want same properties except make the default really slow
        super().__init__(images, xpos, ypos, maxHealth,
                resistance, damage, range, speed,
                attackSpeed, direction)

    # OVERRIDE
    def update(self, direction, obstacles, entities):
        """ Move this enemy according to its AI. This is the same algorithm as the pawn,
            just targetting the player """

        # Note that the passed movement direction is completely ignored.
        #  Movement and actions are controlled by the AI
        direction = None

        # Find all the the directions that yield vlaid motion
        possibleDirections = []

        for d in dirsAsArray():
            if (self.motionIsValid(d, obstacles)):
                possibleDirections.append(d)

        # Find the player in the list of entities
        player = None

        for e in entities:
            if (isinstance(e, Player)):
                player = e

        if (player == None):

            # The player is not present or dead, so don't bother moving
            direction = None

        elif (self.distance(player) < self.range):

            # If they can successfully attack the player, do so
            self.attack(entities, obstacles)

        else:

            # Need to get to the player

            # For each direction, make a dummy sprite and check if this
            #  direction gets the pawn closer. Find the best direction
            #  to go to get to the player

            direction = possibleDirections[0]
            shortDist = 400000000000 # Really big number

            for dir in possibleDirections:
                xChange, yChange = self.getChangeFromDir(dir)
                dummySprite = Sprite(self.x + xChange, self.y + yChange)
                if dummySprite.distance(player) < shortDist:
                    shortDist = dummySprite.distance(player)
                    direction = dir
        
        super().update(direction, obstacles, entities)


    def motionIsValid(self, direction, obstacles):
        """ Checks to see if moving in this direction results in a change in
        position """

        # If there is no direction, moving doesn't change location
        if direction == None:
            return False

        # Get the maximum change in location for the movement direction
        xChange, yChange  = self.getChangeFromDir(direction)

        # Make a dummy sprite to check the collisions
        possible = Sprite(self.x, self.y)

        # Apply vertical movement. If this means it is now colliding,
        #  snap to grid vertically.
        possible.y += yChange
        if possible.isColliding(obstacles):
            possible.y = int(possible.y/BOX_SIZE)*BOX_SIZE + round(possible.y/BOX_SIZE - int(possible.y/BOX_SIZE))*BOX_SIZE

        # Same except horizontally
        possible.x += xChange
        if possible.isColliding(obstacles):
            possible.x = int(possible.x/BOX_SIZE)*BOX_SIZE + round(possible.x/BOX_SIZE - int(possible.x/BOX_SIZE))*BOX_SIZE

        # If the motion would put the enemy in roughly the same place, this
        #  doesn't count as a valid motion. Otherwise, it is
        if (int(possible.x) == int(self.x)
            and int(possible.y) == int(self.y)):
            return False
        return True
    
    def getChangeFromDir(self, direction):

        # Used to store the maximum movement in each direction
        yChange = 0
        xChange = 0

        if direction == Direction.UP:
            yChange = self.speed
        elif direction == Direction.UP_RIGHT:
            yChange = self.speed/2**(1/2)
            xChange = self.speed/2**(1/2)
        elif direction == Direction.RIGHT:
            xChange = self.speed
        elif direction == Direction.DOWN_RIGHT:
            yChange = -self.speed/2**(1/2)
            xChange = self.speed/2**(1/2)
        elif direction == Direction.DOWN:
            yChange = -self.speed
        elif direction == Direction.DOWN_LEFT:
            yChange = -self.speed/2**(1/2)
            xChange = -self.speed/2**(1/2)
        elif direction == Direction.LEFT:
            xChange = -self.speed
        elif direction == Direction.UP_LEFT:
            yChange = self.speed/2**(1/2)
            xChange = -self.speed/2**(1/2)
        
        return (xChange, yChange)
