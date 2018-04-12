# Author: David Thompson
# Date: 6 April, 2018

# Note: Most of the code to interact with pygame such as the initialization
#       and parts of the gameloop, as well as the getResourcePath function
#       are copied from my FlapPY game: https://github.com/datho7561/FlapPY


import pygame, sys, os

from Sprite import Sprite

BOX_SIZE = 32

BOXES_WIDE, BOXES_HIGH = 16, 9

SIZE = WIDTH, HEIGHT = BOX_SIZE*BOXES_WIDE, BOX_SIZE*BOXES_HIGH

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
    file = open(filepath, r)
    file.read()

    # Create variables to store the map information
    background = []
    foreground = []
    decoration = []
    objects = []

    # Go through and read the
    for line in file:

        # Clean up each line
        line.split(",")
        cleanedLine = []

        for element in line:
            element.strip()
            cleanedLine.append(int(element))


    # TODO: change to output four arrays: background, foreground, decorations, and game object links
    return None

## INITIALIZE PYGAME ##

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
pygame.display.set_caption("Fourseal")
screen = pygame.display.set_mode(SIZE)

# Load images

defaultImg = pygame.image.load(getResourcePath("assets\default.png"))
defaultImg.convert()

# Create the sprite list

sprites = []

# Create an array of Sprites to represent the background
for ix in range(BOXES_WIDE):
    for iy in range(BOXES_HIGH):
        sprites.append( Sprite(BOX_SIZE*ix, BOX_SIZE*iy, defaultImg) )

while True:

    pygame.time.Clock().tick(75)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the close button is pressed, exit the program
            sys.exit()

    # TODO: code game logic and graphics

    # Draw the sprites to screen
    Sprite.sort_depth(sprites)
    for s in sprites:
        s.draw(screen)

    pygame.display.flip()
