# Author: David Thompson
# Date: 18 June, 2018

from constants import *
from entity import Entity
from sprite import Sprite
from direction import Direction
from direction import perpendicular, opposite
import random

class Enemy(Entity):

    # OVERRIDE
    def update(self, direction, obstacles, entities):
        """ Move this enemy according to its AI """

        # Note that the passed movement direction is completely ignored
        direction = None

        if self.motionIsValid(self.direction, obstacles):
            direction = self.direction
        else:
            try:
                # Pick a direction that will not result in running
                directionsToGo = list(Direction)
                random.shuffle(directionsToGo)

                for dir in directionsToGo:
                    if self.motionIsValid(dir, obstacles):
                        direction = dir
            except:
                # If the enemy has yet to move, give it
                #  a random initial motion
                direction = random.choice(list(Direction))

        super().update(direction, obstacles, entities)


    def motionIsValid(self, direction, obstacles):
        """ Checks to see if moving in this direction results in a change in
        position """

        # If there is no direction, moving doesn't change location
        if direction == None:
            return False

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
