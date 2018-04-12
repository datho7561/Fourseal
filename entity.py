# Author: David Thompson
# Date: 5 April, 2018

from sprite import Sprite

class Entity(Sprite):

    """ Describes a being that can exist in the game, whether it's a player,
    enemy, or non-player character """

    def __init__(self, xpos = 0, ypos = 0, images[], maxHealth = 100,
                resistance = 20, damage = 25, range = 5, speed = 5):
        """ Creates a new entity. The default is a dummy at (0,0) """

        # Sets this up as a sprite
        super(xpos, ypos, images[])

        # Sets up additional variables
        self.maxHealth = maxHealth
        self.resistance = resistance
        self.killsSinceDeath = 0
        self.health = maxHealth
        self.damage = damage
        self.range = range
        self.speed = speed
        self.dead = False


    def setPos(self, newX, newY):
        """ Changes the position of the Entity, for use in setting up
        the game and teleporting """

        self.x = newX
        self.y = newY


    def attack(self, entities):
        """ Attacks all entities within range of this one. Kills them if
        they need to be dead. """

        for e in entities:

            if self.distance(e) > self.range:
                e.health -= self.damage - e.resistance

                if e.health <= 0:
                    self.killsSinceDeath += 1
                    e.dead = True
                    e.killsSinceDeath = 0


    def move(self, direction):

        # TODO: make the guy hecking move
        pass
