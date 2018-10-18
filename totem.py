# Author:   David Thompson
# Date:     24 September, 2018

from entity import Entity

class Totem(Entity):

    def __init__(self, images, xpos, ypos, health):
        """ Make a totem with given location and health """

        # Speed is zero so that nothing can move this totem
        super().__init__(images, xpos, ypos, speed=0)

    # OVERRIDE
    def attack(self):
        """ The totem should be unable to attack """
        return False

    