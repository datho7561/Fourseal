# Author: David Thompson
# Date: 6 April, 2018
# Note: Most of the code to interact with pygame such as the initialization
#       and parts of the gameloop, as well as the getResourcePath function
#       are copied from my FlapPY game: https://github.com/datho7561/FlapPY


import pygame, sys, os

from pygame import Color
from random import randint, random

from sprite import Sprite, sortSprites
from entity import Entity

from player import Player

# Totem
from totem import Totem

# Characters
from foursealer import Foursealer
from threemason import Threemason
from dialic import Dialic

# Baddies
from pawn import Pawn
from bishop import Bishop
from enemy import Enemy

# UI elements
from menu import menu
from damagebar import DamageBar

from direction import Direction

from map import Map
from constants import *

def getResourcePath(name):
    """ Function to get a resource that's in the same folder as the script """

    return os.path.join(os.path.realpath(__file__)[0:len(os.path.realpath(__file__))-len(os.path.basename(__file__))], name)

def readMapFile(name):
    """ Given the file name, reads the corresponding map file and loads it into memory. """

    # Open the map file abd read it
    filepath = getResourcePath(os.path.join("maps", name))
    file = open(filepath, 'r')
    data = file.read()

    return Map(data)

def loadImage(name):
    """ Loads the given image resource """

    image = pygame.image.load(getResourcePath(os.path.join("assets", name)))
    image.convert_alpha()

    return image

def borderCoords():
    """ Gives a randon coordinate pair along the borders """

    # generate a random number to indicate side
    side = randint(1, 4)

    # intepret results
    if (side == 1):
        # TOP
        return (int(random() * WIDTH), 0)
    elif (side == 2):
        # RIGHT
        return (WIDTH, int(random() * HEIGHT))
    elif (side == 3):
        # BOTTOM
        return (int(random() * WIDTH), HEIGHT)
    else:
        # LEFT
        return (0, int(random() * HEIGHT))



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

totemSprite = loadImage("totem.png")
pawnSprite = loadImage(os.path.join("pawn", "pawn_0.png"))
bishopSprite = loadImage(os.path.join("bishop", "bishop_0.png"))

# "Player" Sprites
# TODO: replace with individual character's textures
playerSprite = loadImage(os.path.join("player", "player_0.png"))

# This font is used for game over
theFont = pygame.font.SysFont("Consolas", 250)

# TODO: add more players
# Create the player(s)


# TODO: read totem location and health from the map file
totem = Totem(totemSprite, WIDTH//2, HEIGHT//2, 200)

# TODO: intelligent enemies that spawn periodically
enemies = []
enemyCooldown = ENEMY_TIME

# TODO: centralize UI creation

# TODO: figure out how many players/enemies/other things
#        there are and add health bars to all of them
playerHB = DamageBar(0, 0)
playerCDB = DamageBar(0, 20, 10, Color(200, 200, 255), Color("blue"))
totemHB = DamageBar(WIDTH//2, 0)

# Initialize the keyboard key variables
# W, D, A, S, Shift, Space
P1KEYS = [False, False, False, False, False, False]

# Load the default map with all the default textures

theMap = readMapFile("1.4clmap")

background = theMap.getBg(textures)
fgSprites = theMap.getFg(textures)

# Create the sprite list

sprites = []

sprites.append(totem)
sprites += fgSprites

# Create the entity list
entities = []

entities.append(totem)

# Character select loop
playerType = menu(screen)

# TODO: Finish character and game setup before starting the game


# TODO: let player pick in windowed app
if (playerType == "T"):
    player = Threemason(playerSprite, BOX_SIZE, BOX_SIZE)
elif (playerType =="D"):
    player = Dialic(playerSprite, BOX_SIZE, BOX_SIZE)
elif (playerType == "F"):
    player = Foursealer(playerSprite, BOX_SIZE, BOX_SIZE)
else:
    player = Foursealer(playerSprite, BOX_SIZE, BOX_SIZE)

entities.append(player)
sprites.append(player)


# Main loop

gameRunning = True

while True:

    pygame.time.Clock().tick(75)

    if gameRunning:

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
            player.attack(entities, fgSprites)

        player.update(player1Dir, fgSprites, entities, usingSpecial = P1KEYS[4])

        # If it is time to add another foes, add one
        if (enemyCooldown == 0):

            # Chose type of enemy
            typeNewEnemy = randint(0, 9)

            # Figure out where the foe goes
            newEnemyX, newEnemyY = borderCoords()

            # Make the enemy
            # TODO: make other types of enemies appear

            # Bishop, which follows player, is rarer than pawn
            if (typeNewEnemy == 9):
                newEnemy = Bishop(bishopSprite, newEnemyX, newEnemyY)
            else:
                newEnemy = Pawn(pawnSprite, newEnemyX, newEnemyY)

            # Add the new foe to the necessary lists
            enemies.append(newEnemy)
            sprites.append(newEnemy)
            entities.append(newEnemy)

            enemyCooldown = ENEMY_TIME

        else:
            # Otherwise just count down
            enemyCooldown -= 1

        for enemy in enemies:
            enemy.update(None, fgSprites, entities)

        # Remove dead entities from list
        allDeadRemoved = False

        while not allDeadRemoved:

            # Find the first dead entity in the list
            toRemove = None
            for e in entities:
                if e.dead:
                    toRemove = e
                    break
            
            if toRemove == None:
                # If no dead entities were found, flag for the loop to end
                allDeadRemoved = True
            else:
                # Otherwise remove the found entity and proceed with the loop
                entities.remove(toRemove)
        
        
        ## DRAW ##

        # TODO: draw everything

        # DRAW THE BACKGROUND #
        screen.blit(background, (0,0))

        # DRAW THE SPRITES #
        sortSprites(sprites)
        for s in sprites:
            s.draw(screen)

        # DRAW THE HUD #

        # TODO: Draw image representations of the players faces
        # TODO: automate health bar drawing of everyone

        playerHB.update(player)
        playerCDB.update(player.attackTimer / player.attackSpeed)
        totemHB.update(totem)
        
        playerHB.draw(screen)
        playerCDB.draw(screen)
        totemHB.draw(screen)

        # Draw the GAME OVER
        if (player.dead or totem.dead):
            txtPlacement = (WIDTH // 2) - (theFont.size("FAILURE")[0] // 2)
            screen.blit(theFont.render("FAILURE", False, Color("red")), (txtPlacement,HEIGHT//2-125))
            gameRunning = False


        # Update the double buffer
        pygame.display.flip()

    else:

        # If the game is complete wait for exit

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the close button is pressed, exit the program
                sys.exit()
