# Author: David Thompson
# Date: 5 April, 2018

from sprite import Sprite
from direction import Direction
from constants import *

class Entity(Sprite):

    """ Describes a being that can exist in the game, whether it's a player,
    enemy, or non-player character """

    def __init__(self, images, xpos = 0, ypos = 0, maxHealth = 100,
                resistance = 20, damage = 25, range = 5, speed = 3,
                attackSpeed = 45, direction = None):
        """ Creates a new entity. The default is a dummy at (0,0) """

        # Sets this up as a sprite
        super().__init__(xpos, ypos, images)

        # Sets up additional variables
        self.maxHealth = maxHealth
        self.resistance = resistance
        self.health = maxHealth
        self.damage = damage
        self.range = range
        self.speed = speed
        self.direction = direction
        self.attackSpeed = attackSpeed

        # These variables don't need to be initalized to any other value
        self.killsSinceDeath = 0
        self.dead = False
        self.step = 0
        self.attackTimer = 0


    def setPos(self, newX, newY):
        """ Changes the position of the Entity, for use in setting up
        the game and teleporting """

        self.x = newX
        self.y = newY


    def attack(self, entities):
        """ Attacks all entities within range of this one. Kills them if
        they need to be dead. Returns True if the attack is successful. """

        # TODO: make the entity only attack in fron of them

        if self.attackTimer == 0:

            for e in entities:

                if self.distance(e) < self.range:
                    e.health -= self.damage - e.resistance

                    if e.health <= 0:
                        e.health = 0
                        self.killsSinceDeath += 1
                        e.dead = True
                        e.killsSinceDeath = 0

            self.attackTimer = self.attackSpeed

            return True

        return False


    def move(self, direction, obstacles):
        """ Move the entity in the given direction """

        # If there is not direction, don't bother trying to move
        if direction == None:
            return

        # Find which direction the entity is moving and figure out what
        #  sequence of movements that corresponds to.
        self.direction = direction

        yChange = 0
        xChange = 0

        if direction == Direction.UP:
            yChange = self.speed
        elif direction == Direction.UP_RIGHT:
            yChange = self.speed/2**(1/2)
            xChange = self.speed/2**(1/2)
        elif direction == Direction.RIGHT:
            xChange = self.speed
        elif direction == Direction.DOWN_RIGHT:
            yChange = -self.speed/2**(1/2)
            xChange = self.speed/2**(1/2)
        elif direction == Direction.DOWN:
            yChange = -self.speed
        elif direction == Direction.DOWN_LEFT:
            yChange = -self.speed/2**(1/2)
            xChange = -self.speed/2**(1/2)
        elif direction == Direction.LEFT:
            xChange = -self.speed
        elif direction == Direction.UP_LEFT:
            yChange = self.speed/2**(1/2)
            xChange = -self.speed/2**(1/2)

        # Apply vertical movement. If this means it is now colliding,
        #  snap to grid vertically.
        self.y += yChange
        if self.isColliding(obstacles):
            self.y = int(self.y/BOX_SIZE)*BOX_SIZE + round(self.y/BOX_SIZE - int(self.y/BOX_SIZE))*BOX_SIZE

        # Same except horizontally
        self.x += xChange
        if self.isColliding(obstacles):
            self.x = int(self.x/BOX_SIZE)*BOX_SIZE + round(self.x/BOX_SIZE - int(self.x/BOX_SIZE))*BOX_SIZE

        # Take a step
        self.step += 1
        if self.step >= 23:
            self.step = 0


    def update(self, direction, obstacles, entities):
        """ Update this entity: do everything that doesn't involve drawing.
        Should be performed every frame """

        # TODO: handle attacking and prevent movement during attack

        if (self.attackTimer == 0):
            self.move(direction, obstacles)
        else:
            self.attackTimer -= 1


    # OVERRIDE
    def draw(self, surface):
        """ Draws the entity to the surface """

        if not self.dead:

            # TODO: handle the sprites for the entity to attack

            # Calculate direction modifier

            if self.direction == Direction.UP or self.direction == Direction.UP_LEFT or self.direction == Direction.UP_RIGHT:
                directionModifier = 0
            elif self.direction == Direction.RIGHT:
                directionModifier = 1
            elif self.direction == Direction.DOWN or self.direction == Direction.DOWN_LEFT or self.direction == Direction.DOWN_RIGHT:
                directionModifier = 2
            else:
                directionModifier = 3

            # Calculate step modifier

            stepModifier = self.step//6
            if stepModifier%2 == 1:
                stepModifier = 1

            # Select the appropriate texture
            texture = directionModifier * 3 + stepModifier
            super().draw(surface, textureNum = texture)
