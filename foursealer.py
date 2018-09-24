# Author: David Thompson
# Date: 18 June, 2018

from player import Player
from constants import *

class Foursealer(Player):

    def __init__(self, images, xpos, ypos):

        super().__init__(images, xpos, ypos,
                        maxHealth = 100,        # Values for character contants
                        resistance = 25,
                        damage = 50,
                        range = 60,
                        speed = 2,
                        attackSpeed = 45,
                        specialCooldown = 150)

    # OVERRIDE
    def special(self, direction, obstacles, entities):

        # If within the first 10 frames of the burst
        if self.specialTimer > self.specialCooldown - 10:
            # Move in the direction that the player was facing
            #  when the special was initiated. Move them 3 times what they
            #  normally would move. Note that this prevents clipping
            #  through walls because the player is moving in short steps
            for i in range(3):
                self.move(self.direction, obstacles)
            

            # Attack during the dash at four time the speed
            if self.attack(entities):
                self.attackTimer = self.attackSpeed // 4
            
            # If the player is still moving forward, prevent them from changing directions
            return None

        # If the burst of movement is done, allow the player to move as normal
        return direction
