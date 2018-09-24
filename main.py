# Author: David Thompson
# Date: 6 April, 2018
# Note: Most of the code to interact with pygame such as the initialization
#       and parts of the gameloop, as well as the getResourcePath function
#       are copied from my FlapPY game: https://github.com/datho7561/FlapPY


import pygame, sys, os

from sprite import Sprite, sortSprites
from entity import Entity
from player import Player
from enemy import Enemy

from foursealer import Foursealer
from threemason import Threemason
from dialic import Dialic

from direction import Direction

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
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images

textures = []

for i in range(16):
    textures.append(loadImage(str(i) + ".png"))

playerSprites = []

for i in range(12):
    playerSprites.append(loadImage("player\\player_" + str(i) + ".png"))

# Create the fonts

theFont = pygame.font.SysFont("monospace", 16)

# TODO: add more players
# Create the player(s)

# TODO: let the player pick what they play as in a nicer way
playerType = input("Please input (T)hreemason, (D)ialic, or (F)oursealer: ")

if (playerType == "T"):
    player = Threemason(playerSprites, BOX_SIZE, BOX_SIZE)
elif (playerType =="D"):
    player = Dialic(playerSprites, BOX_SIZE, BOX_SIZE)
elif (playerType == "F"):
    player = Foursealer(playerSprites, BOX_SIZE, BOX_SIZE)
else:
    player = Foursealer(playerSprites, BOX_SIZE, BOX_SIZE)

# TODO: intelligent enemies that spawn periodically
enemy = Enemy(playerSprites, 4*BOX_SIZE, 4*BOX_SIZE)

# Initialize the keyboard key variables
# W, D, A, S, Shift, Space
P1KEYS = [False, False, False, False, False, False]

# Load the default map with all the default textures

theMap = readMapFile("0.4clmap")

background = theMap.getBg(textures)
fgSprites = theMap.getFg(textures)

# Create the sprite list

sprites = []

sprites.append(player)
sprites.append(enemy)
sprites += fgSprites

while True:

    pygame.time.Clock().tick(75)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the close button is pressed, exit the program
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == 119:
                # If 'w' is pressed
                P1KEYS[0] = True
            elif event.key == 100:
                # If 'd' is pressed
                P1KEYS[1] = True
            elif event.key == 115:
                # If 's' is pressed
                P1KEYS[2] = True
            elif event.key == 97:
                # If 'a' is pressed
                P1KEYS[3] = True
            elif event.key == 304:
                # If 'Shift' is pressed
                P1KEYS[4] = True
            elif event.key == 32:
                # If 'Space' is pressed
                P1KEYS[5] = True

        elif event.type == pygame.KEYUP:

            if event.key == 119:
                # If 'w' is pressed
                P1KEYS[0] = False
            elif event.key == 100:
                # If 'd' is pressed
                P1KEYS[1] = False
            elif event.key == 115:
                # If 's' is pressed
                P1KEYS[2] = False
            elif event.key == 97:
                # If 'a' is pressed
                P1KEYS[3] = False
            elif event.key == 304:
                # If 'Shift' is pressed
                P1KEYS[4] = False
            elif event.key == 32:
                # If 'Space' is pressed
                P1KEYS[5] = False


    # TODO: code game logic
    ## GAME LOGIC ##

    # Interpret player input

    # Player 1

    player1Dir = None

    if P1KEYS[0] and P1KEYS[1]:
        player1Dir = Direction.UP_RIGHT
    elif P1KEYS[1] and P1KEYS[2]:
        player1Dir = Direction.DOWN_RIGHT
    elif P1KEYS[2] and P1KEYS[3]:
        player1Dir = Direction.DOWN_LEFT
    elif P1KEYS[3] and P1KEYS[0]:
        player1Dir = Direction.UP_LEFT
    elif P1KEYS[0]:
        player1Dir = Direction.UP
    elif P1KEYS[1]:
        player1Dir = Direction.RIGHT
    elif P1KEYS[2]:
        player1Dir = Direction.DOWN
    elif P1KEYS[3]:
        player1Dir = Direction.LEFT

    # TODO: update all the players
    # Update the players

    if P1KEYS[5]:
        player.attack([enemy])

    player.update(player1Dir, fgSprites, [enemy], usingSpecial = P1KEYS[4])

    enemy.update(None, fgSprites, [player])

    # TODO: draw everything
    ## DRAW ##

    # Draw the background
    screen.blit(background, (0,0))

    # Draw the sprites to screen
    sortSprites(sprites)
    for s in sprites:
        s.draw(screen)

    # Draw the HUD
    playerHealthHUD = theFont.render(str(player.health), 1, (255,0,255), (0,0,0))
    enemyHealthHUD = theFont.render(str(enemy.health), 1, (255,0,255), (0,0,0))

    screen.blit(playerHealthHUD, (0,0))
    screen.blit(enemyHealthHUD, (250,0))

    # Update the double buffer
    pygame.display.flip()
