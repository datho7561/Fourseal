# Author: David Thompson
# Date: 6 April, 2018

# Note: Most of the code to interact with pygame such as the initialization
#       and parts of the gameloop, as well as the getResourcePath function
#       are copied from my FlapPY game: https://github.com/datho7561/FlapPY


import pygame, sys, os

from sprite import Sprite
from map import Map
from constants import *

def getResourcePath(name):
    """ Function to get a resource that's in the same folder as the script """

    # Important for pyinstaller
    if getattr(sys, 'frozen', False):
        return (os.path.realpath(sys._MEIPASS)[0:len(os.path.realpath(sys._MEIPASS))-len(os.path.basename(sys._MEIPASS))] + name)
    else:
        return (os.path.realpath(__file__)[0:len(os.path.realpath(__file__))-len(os.path.basename(__file__))] + name)

def readMapFile(name):
    """ Given the file name, reads the corresponding map file and loads it into memory. """

    # Open the map file abd read it
    filepath = getResourcePath("maps\\" + name)
    file = open(filepath, 'r')
    data = file.read()

    return Map(data)

def loadImage(name):
    """ Loads the given image resource """

    image = pygame.image.load(getResourcePath("assets\\" + name))
    image.convert_alpha()

    return image


## INITIALIZE PYGAME ##

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
pygame.display.set_caption("Fourseal")
screen = pygame.display.set_mode((2*WIDTH, 2*HEIGHT))

# Load images

textures = []

for i in range(16):
    textures.append(loadImage(str(i) + ".png"))

# Create the sprite list

sprites = []

# Load the default map with all the default textures

theMap = readMapFile("0.4clmap")

background = theMap.getBg(textures)
fgSprites = theMap.getFg(background, textures)

while True:

    pygame.time.Clock().tick(75)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the close button is pressed, exit the program
            sys.exit()

    # TODO: code game logic and graphics

    # Draw the hecking background

    screen.blit(pygame.transform.scale(background, (2*WIDTH, 2*HEIGHT)), (0,0))

    # Draw the sprites to screen
    # Sprite.sort_depth(sprites)
    # for s in sprites:
    #     s.draw(screen)

    pygame.display.flip()
