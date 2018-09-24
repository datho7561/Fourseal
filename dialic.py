# Author: David Thompson
# Date: 23 August, 2018

from player import Player
from constants import *

class Dialic(Player):

    def __init__(self, images, xpos, ypos):

        super().__init__(images, xpos, ypos,
                        maxHealth = 100,        # Values for character contants
                        resistance = 15,
                        damage = 0,             # This value gets changed in this character
                        range = 35,
                        speed = 0,              # This value gets changed in this character
                        attackSpeed = 0,        # This value gets changed in this character
                        specialCooldown = 10)   # Almost instantaneous reactivation

        self.strengthMoveSpeed = 2
        self.strengthAttackSpeed = 30
        self.strengthDamage = 35

        self.speedMoveSpeed = 6
        self.speedAttackSpeed = 3
        self.speedDamage = 20

        self.speed = self.speedMoveSpeed
        self.attackSpeed = self.speedAttackSpeed
        self.damage = self.speedDamage

        self.isStrong = False

    # OVERRIDE
    def special(self, direction, obstacles, entities):

        # TODO: implement special

        # Switch between speed and strength modes
        self.isStrong = not self.isStrong

        if (self.isStrong):
            self.speed = self.strengthMoveSpeed
            self.attackSpeed = self.strengthAttackSpeed
            self.damage = self.strengthDamage
        else:
            self.speed = self.speedMoveSpeed
            self.attackSpeed = self.speedAttackSpeed
            self.damage = self.speedDamage

        return direction
