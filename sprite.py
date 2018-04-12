# Author: David Thompson
# Date: 5 April, 2018

from pygame import Surface

class Sprite:

    """ Represents an object that has a position on the screen and
    image that is associated with it """

    global BOX_SIZE
    BOX_SIZE = 32

    def __init__(self, xpos = 0, ypos = 0, images = None):
        """ Creates a new sprite. """
        self.x = xpos
        self.y = ypos

        self.imgs = images
        if images == None:
            self.imgs = []


    def draw(self, surface):
        """ Draws this in place onto the given surface. Notice how this flips
        everything arouns so that the zero in the the y direction is
        in the bottom left of the screen. """

        try:
            if self.imgs == []:
                raise IndexError
            else:
                surface.blit(self.imgs[0], (int(self.x), surface.get_size()[1] - int(self.y) - BOX_SIZE))

        except TypeError as e:
            surface.blit(self.imgs, (int(self.x), surface.get_size()[1] - int(self.y) - BOX_SIZE))


    def distance(self, other):
        """ Finds the distance between this Sprite and another one. """
        return ((other.x-self.x)**2 + (other.y-self.y)**2)**(1/2)

    def sort_depth(sprites):
        """ Sorts a list of sprites so that they can be drawn from the back to the front. """
        sprites.sort(key = lambda sprite: sprite.y, reverse = True)


if __name__ == "__main__":

    mySprite = Sprite()
    myOtherSprite = Sprite(4, 4)

    print(mySprite.distance(myOtherSprite))
