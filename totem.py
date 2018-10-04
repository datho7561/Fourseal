# Author:   David Thompson
# Date:     24 September, 2018

from entity import Entity

class Totem(Entity):

    def __init__(self, images, xpos, ypos, health):
        """ Make a totem with given location and health """

        super().__init__(images, xpos, ypos)

    # OVERRIDE
    def attack(self):
        """ The totem should be unable to attack """
        return False

    