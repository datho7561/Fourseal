# Author: David Thompson
# Date: 5 April, 2018

import random

from pygame import Surface
from constants import *

class Sprite:

    """ Represents an object that has a position on the screen and
    image that is associated with it """

    def __init__(self, xpos = 0, ypos = 0, images = None):
        """ Creates a new sprite. """
        self.x = xpos
        self.y = ypos

        self.imgs = images
        if images == None:
            self.imgs = []


    def draw(self, surface, shift=False):
        """ Draws this in place onto the given surface. Notice how this flips
        everything arouns so that the zero in the the y direction is
        in the bottom left of the screen. """

        # Shift the texture off a bit randomly if it is set to
        x_shift, y_shift = 0, 0
        if shift:
            x_shift, y_shift = random.randrange(-3,4), random.randrange(-3,4)

        try:
            if self.imgs == []:
                raise IndexError
            else:
                surface.blit(self.imgs[0], (int(self.x) + x_shift,
                            surface.get_size()[1] - int(self.y) - self.imgs[0].get_size()[1] + BOX_SIZE + y_shift))

        except TypeError as e:
            surface.blit(self.imgs, (int(self.x) + x_shift,
                        surface.get_size()[1] - int(self.y) - self.imgs.get_size()[1] + y_shift))


    def distance(self, other):
        """ Finds the distance between this Sprite and another one. """
        return ((other.x-self.x)**2 + (other.y-self.y)**2)**(1/2)

    def isColliding(self, other):
        """ Checks if the two Sprites are colliding """
        # TODO: prove that this actually works and isn't just spaghet
        return (abs(self.x - other.x) < BOX_SIZE and abs(self.y - other.y) < BOX_SIZE)


    def sort_depth(sprites):
        """ Sorts a list of sprites so that they can be drawn from the back to the front. """
        sprites.sort(key = lambda sprite: sprite.y, reverse = True)

# Used to test the class
if __name__ == "__main__":

    mySprite = Sprite()
    myOtherSprite = Sprite(4, 4)

    print(mySprite.distance(myOtherSprite))
