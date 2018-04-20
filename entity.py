# Author: David Thompson
# Date: 5 April, 2018

from sprite import Sprite
from direction import Direction

class Entity(Sprite):

    """ Describes a being that can exist in the game, whether it's a player,
    enemy, or non-player character """

    def __init__(self, images, xpos = 0, ypos = 0, maxHealth = 100,
                resistance = 20, damage = 25, range = 5, speed = 3, direction = 0):
        """ Creates a new entity. The default is a dummy at (0,0) """

        # Sets this up as a sprite
        super().__init__(xpos, ypos, images)

        # Sets up additional variables
        self.maxHealth = maxHealth
        self.resistance = resistance
        self.killsSinceDeath = 0
        self.health = maxHealth
        self.damage = damage
        self.range = range
        self.speed = speed
        self.direction = direction
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
        """ Move the entity in the given direction """

        # TODO: collision with the world, either here or in the main class

        self.direction = direction.value

        # Move the player in the desired direction
        if direction == Direction.UP:
            self.y += self.speed
        elif direction == Direction.UP_RIGHT:
            self.y += self.speed/2**(1/2)
            self.x += self.speed/2**(1/2)
        elif direction == Direction.RIGHT:
            self.x += self.speed
        elif direction == Direction.DOWN_RIGHT:
            self.y -= self.speed/2**(1/2)
            self.x += self.speed/2**(1/2)
        elif direction == Direction.DOWN:
            self.y -= self.speed
        elif direction == Direction.DOWN_LEFT:
            self.y -= self.speed/2**(1/2)
            self.x -= self.speed/2**(1/2)
        elif direction == Direction.LEFT:
            self.x -= self.speed
        elif direction == Direction.UP_LEFT:
            self.y += self.speed/2**(1/2)
            self.x -= self.speed/2**(1/2)

    # OVERRIDES PARENT
    def draw(self, surface):

        # Select the texture that corresponds to the direction the entity is facing
        texture = self.direction
        super().draw(surface, textureNum = texture)
