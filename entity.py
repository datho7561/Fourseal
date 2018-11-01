# Author: David Thompson
# Date: 5 April, 2018

from sprite import Sprite
from direction import Direction
from direction import opposite
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
        self.recoilTimer = 0
        self.reDir = None


    def setPos(self, newX, newY):
        """ Changes the position of the Entity, for use in setting up
        the game and teleporting """

        self.x = newX
        self.y = newY


    def attack(self, entities, obstacles):
        """ Attacks all entities within range of this one. Kills them if
        they need to be dead. Returns True if the attack is successful. """

        # TODO: make the entity only attack in front of themselves

        # The entity needs to be alive and cooled down to attack
        if not self.dead and self.attackTimer == 0:

            for e in entities:

                # If this entity isn't itself and it is within range
                if not self is e and self.distance(e) < self.range:

                    # Check if damage is actually going to be done. Otherwise,
                    #  no recoil nor killing
                    if not self.damage - e.resistance == 0:
                        e.health -= self.damage - e.resistance

                        # If the entity gets killed, 
                        if e.health <= 0:
                            e.health = 0                # make sure health isn't negative
                            self.killsSinceDeath += 1   # increment the killer's kills since death
                            e.dead = True               # set the other entity to dead
                            e.killsSinceDeath = 0       # the other entity's kill count is zero
                        else:
                            e.recoilTimer = RECOIL      # The entity must face recoil
                            e.reDir = self.direction    # Pass own direction as entities recoil

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


    def recoil(self, obstacles):
        """ Move the player backwards due to a previous attack """

        yChange = 0
        xChange = 0

        # Figure out what change in coords is necessary for the recoil
        if self.reDir == Direction.UP:
            yChange = RECOIL_SPEED
        elif self.reDir == Direction.UP_RIGHT:
            yChange = RECOIL_SPEED/2**(1/2)
            xChange = RECOIL_SPEED/2**(1/2)
        elif self.reDir == Direction.RIGHT:
            xChange = RECOIL_SPEED
        elif self.reDir == Direction.DOWN_RIGHT:
            yChange = -RECOIL_SPEED/2**(1/2)
            xChange = RECOIL_SPEED/2**(1/2)
        elif self.reDir == Direction.DOWN:
            yChange = -RECOIL_SPEED
        elif self.reDir == Direction.DOWN_LEFT:
            yChange = -RECOIL_SPEED/2**(1/2)
            xChange = -RECOIL_SPEED/2**(1/2)
        elif self.reDir == Direction.LEFT:
            xChange = -RECOIL_SPEED
        elif self.reDir == Direction.UP_LEFT:
            yChange = RECOIL_SPEED/2**(1/2)
            xChange = -RECOIL_SPEED/2**(1/2)

        # Apply vertical movement. If this means it is now colliding,
        #  snap to grid vertically.
        self.y += yChange
        if self.isColliding(obstacles):
            self.y = int(self.y/BOX_SIZE)*BOX_SIZE + round(self.y/BOX_SIZE - int(self.y/BOX_SIZE))*BOX_SIZE

        # Same except horizontally
        self.x += xChange
        if self.isColliding(obstacles):
            self.x = int(self.x/BOX_SIZE)*BOX_SIZE + round(self.x/BOX_SIZE - int(self.x/BOX_SIZE))*BOX_SIZE


    def update(self, direction, obstacles, entities):
        """ Update this entity: do everything that doesn't involve drawing.
        Should be performed every frame """

        # TODO: handle attacking and prevent movement during attack

        if (self.recoilTimer > 0):
            self.recoilTimer -= 1 # Adavance to next fram of recoil
            self.recoil(obstacles) # Perform the recoil action
        elif (self.attackTimer == 0):
            self.move(direction, obstacles)
        else:
            self.move(direction, obstacles)
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
