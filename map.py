# Author: David Thompson
# Date: 11 April, 2017

from pygame import Surface
from sprite import Sprite
from constants import *

import math, random

class Map:

    """ Holds the data for an entire game map, and allows the data to be read and accessed easily """

    global SPREAD_MIN, SPREAD_MAX

    SPREAD_MIN, SPREAD_MAX = 80, 150

    def __init__(self, data):
        """ Sets up the map given the data from the map file """

        # Create variables to store the map information
        self.background = []
        self.foreground = []
        self.decoration = []
        self.objects = []

        # Split the data by lines

        cleanedData = data.split('\n')

        # Process data into memory as ints
        # TODO: read more than the first 9 lines
        for i in range(2*BOXES_HIGH):

            # Clean up each line
            line = cleanedData[i].split(",")
            cleanedLine = []

            for element in line:
                cleanedLine.append(int(element.strip()))

            # TODO: read the other information as well
            if (i//BOXES_HIGH == 0):
                self.background.append(cleanedLine)
            elif (i//BOXES_HIGH == 1):
                self.foreground.append(cleanedLine)
            elif (i//BOXES_HIGH == 2):
                self.decoration.append(cleanedLine)
            else:
                self.objects.append(cleanedLine)

    def pixelSpread(num):
        """ A logistic function to control where the pixels are placed.
        Places most of the pixels near the edge. """
        return num**4


    def getBg(self, images):
        """ Returns the background, stitched together and 'nicely' blended """

        bgImage = Surface(SIZE)

        for y in range(BOXES_HIGH):
            for x in range(BOXES_WIDE):

                # Find the texture for this Sprite
                textureNum = self.background[y][x]
                texture = images[textureNum].copy()

                # Edit the pixels based on the textures around

                # In each of the four cardinal directions
                for q in ((-1,0), (1,0), (0,-1), (0, 1)):

                    # Makes sure the spot that s being checked actually exists
                    if (y+q[0] >= 0 and x+q[1] >= 0 and
                        y+q[0] < BOXES_HIGH and x+q[1] < BOXES_WIDE):

                        blendingTextureNum = self.background[y + q[0]][x + q[1]]

                        if blendingTextureNum <= 0 or blendingTextureNum > 9:
                            print(blendingTextureNum)

                        # If the textures are different
                        if (textureNum != blendingTextureNum):

                            numSpread = random.randrange(SPREAD_MIN, SPREAD_MAX)

                            for i in range(numSpread):

                                # Generate a number that is usually just less than 1
                                gamma = Map.pixelSpread(random.random())

                                # Calculate the point
                                if (q==(-1, 0)):
                                    x_comp = int(random.randrange(0, BOX_SIZE))
                                    y_comp = int(gamma*BOX_SIZE / 4)
                                elif (q==(0, -1)):
                                    x_comp = int(gamma*BOX_SIZE / 4)
                                    y_comp = int(random.randrange(0, BOX_SIZE))
                                elif (q==(1,  0)):
                                    x_comp = int(random.randrange(0, BOX_SIZE))
                                    y_comp = BOX_SIZE - 1 - int(gamma*BOX_SIZE / 4)
                                else:
                                    x_comp = BOX_SIZE - 1 - int(gamma*BOX_SIZE / 4)
                                    y_comp = int(random.randrange(0, BOX_SIZE))

                                # “We don't make mistakes,
                                #  just happy little accidents.” - Bob Ross
                                texture.set_at((x_comp, y_comp), (20, 20, 20))

                blockSprite = Sprite(BOX_SIZE * x, BOX_SIZE * (BOXES_HIGH-y-1), texture)

                blockSprite.draw(bgImage)

        return bgImage


    def getFg(self, background, images):
        """ Returns a texture that represents the foreground, as well as a list
        of sprites that represent the objects that can be collided with. """

        # Holds all the sprites that will be used for collision with the player
        fgSprites = []

        for y in range(BOXES_HIGH):
            for x in range(BOXES_WIDE):

                textureNum = self.foreground[y][x]
                texture = images[textureNum].copy()

                drawingSprite = Sprite(BOX_SIZE * x, BOX_SIZE * (BOXES_HIGH-y-1), texture)
                collisionSprite = Sprite(BOX_SIZE * x, BOX_SIZE * (BOXES_HIGH-y-1), texture)
                fgSprites.append(collisionSprite)

                if (textureNum != 0):
                    drawingSprite.draw(background, shift=True)

        return fgSprites
