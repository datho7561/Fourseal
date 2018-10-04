# Author: David Thompson
# Date: 5 April, 2018

import random
import operator

from pygame import Surface
from constants import *

def sortSprites(sprites):
    """ Sorts a list of sprites so that they can be drawn from the back to the front. """

    sprites.sort(key = operator.attrgetter('y'), reverse = True)

class Sprite:

    """ Represents an object that has a position on the screen and
    image that is associated with it """

    def __init__(self, xpos = 0, ypos = 0, images = None, isShifted=False):
        """ Creates a new sprite. """
        self.x = xpos
        self.y = ypos

        self.xShift = 0
        self.yShift = 0

        if isShifted:
            self.xShift, self.yShift = random.randrange(-3,4), random.randrange(-3,4)

        self.isShifted = isShifted

        self.imgs = images
        if images == None:
            self.imgs = []


    def draw(self, surface, textureNum=0):
        """ Draws this in place onto the given surface. Notice how this flips
        everything around so that the zero in the the y direction is
        in the bottom left of the screen. """

        try:
            if self.imgs == []:
                raise IndexError
            else:
                surface.blit(self.imgs[textureNum], (int(self.x) + self.xShift,
                            surface.get_size()[1] - int(self.y) - self.imgs[textureNum].get_size()[1] + self.yShift))

        except TypeError:
            surface.blit(self.imgs, (int(self.x) + self.xShift,
                        surface.get_size()[1] - int(self.y) - self.imgs.get_size()[1] + self.yShift))


    def distance(self, other):
        """ Finds the distance between this Sprite and another one. """
        return ((other.x-self.x)**2 + (other.y-self.y)**2)**(1/2)

    def isColliding(self, other):
        """ Checks if Sprites are colliding """

        try:
            # If it is a list of sprites, go through them all, checking for collisions
            collision = False
            for s in other:
                if (abs(self.x - s.x) < BOX_SIZE and abs(self.y - s.y) < BOX_SIZE):
                    collision = True
                    break

            return collision

        except:
            # If it's just one sprite, just check it
            return (abs(self.x - other.x) < BOX_SIZE and abs(self.y - other.y) < BOX_SIZE)
