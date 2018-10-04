# Author: David Thompson
# Date: 11 April, 2018

from entity import Entity
from totem import Totem

class Player(Entity):

    def __init__(self, images, xpos = 0, ypos = 0, maxHealth = 100,
                resistance = 20, damage = 25, range = 5, speed = 3,
                attackSpeed = 45, direction = 0, specialCooldown = 30,
                specialTimer = 0):

        super().__init__(images, xpos, ypos, maxHealth, resistance, damage,
                            range, speed, attackSpeed, direction)

        self.specialCooldown = specialCooldown
        self.specialTimer = specialTimer


    def special(self, direction, obstacles, entities):
        """ Performs the special move, then returns the direction
        that the player should move after performing it """

        return direction


    # OVERRIDE
    def attack(self, entities, obstacles):

        # A player should not be able to kill their own totem, because
        #  defending the totem is the objective of the player when the
        #  totem is present

        filteredEntities = []
        
        for e in entities:
            if (not isinstance(e, Totem)):
                filteredEntities.append(e)

        super().attack(filteredEntities, obstacles)

    # OVERRIDE
    def update(self, direction, obstacles, entities, usingSpecial):

        if self.specialTimer > 0:
            # If the special is in progress
            self.specialTimer -= 1
            direction = self.special(direction, obstacles, entities)

        elif usingSpecial:
            # If the special button is pressed and cooldown is finished
            self.specialTimer = self.specialCooldown
            direction = self.special(direction, obstacles, entities)

        super().update(direction, obstacles, entities)
