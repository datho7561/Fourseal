# Author: David Thompson
# Date: 18 June, 2018

from player import Player
from constants import *

class Threemason(Player):

    def __init__(self, images, xpos, ypos):

        super().__init__(images, xpos, ypos,
                        maxHealth = 100,        # Values for character contants
                        resistance = 15,
                        damage = 50,
                        range = 40,
                        speed = 2.5,
                        attackSpeed = 30,
                        specialCooldown = 150)

    # OVERRIDE
    def special(self, direction, obstacles, entities):

        # TODO: implement special

        return direction
