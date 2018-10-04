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
from pawn import Pawn

from totem import Totem

# Characters
from foursealer import Foursealer
from threemason import Threemason
from dialic import Dialic

# UI elements
from damagebar import DamageBar

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


# TODO: let the player pick what they play as in a nicer way
playerType = input("Please input (T)hreemason, (D)ialic, or (F)oursealer: ")

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
totemSprites = []

# TODO: make this less dumb e.g. only have one reference to the texture
# TODO: make this an obelisk instead of a vase
for i in range(12):
    totemSprites.append(loadImage("vase.png"))

for i in range(12):
    playerSprites.append(loadImage("player\\player_" + str(i) + ".png"))

# Create the fonts

theFont = pygame.font.SysFont("monospace", 16)

# TODO: add more players
# Create the player(s)


# TODO: let player pick in windowed app
if (playerType == "T"):
    player = Threemason(playerSprites, BOX_SIZE, BOX_SIZE)
elif (playerType =="D"):
    player = Dialic(playerSprites, BOX_SIZE, BOX_SIZE)
elif (playerType == "F"):
    player = Foursealer(playerSprites, BOX_SIZE, BOX_SIZE)
else:
    player = Foursealer(playerSprites, BOX_SIZE, BOX_SIZE)

# TODO: read totem location and health from the map file
totem = Totem(totemSprites, WIDTH//2, HEIGHT//2, 200)

# TODO: intelligent enemies that spawn periodically
enemy = Pawn(playerSprites, 4*BOX_SIZE, 4*BOX_SIZE)

# TODO: centralize UI creation

# TODO: figure out how many players/enemies/other things
#        there are and add health bars to all of them
playerHB = DamageBar(0, 0)
enemyHB = DamageBar(WIDTH - 80, 0)
totemHB = DamageBar(WIDTH//2, 0)

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
sprites.append(totem)
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
        # TODO: player shouldn't be able to attack totem
        player.attack([enemy, totem])

    player.update(player1Dir, fgSprites, [enemy], usingSpecial = P1KEYS[4])

    enemy.update(None, fgSprites, [player, totem])

    # TODO: draw everything
    ## DRAW ##

    # Draw the background
    screen.blit(background, (0,0))

    # Draw the sprites to screen
    sortSprites(sprites)
    for s in sprites:
        s.draw(screen)

    # DRAW THE HUD #

    # TODO: Draw image representations of the players faces
    # TODO: automate health bar drawing of everyone

    playerHB.update(player)
    enemyHB.update(enemy)
    totemHB.update(totem)

    playerHB.draw(screen)
    enemyHB.draw(screen)
    totemHB.draw(screen)

    # Update the double buffer
    pygame.display.flip()
