# Author:    David Thompson
# Date:      26 October, 2018

import pygame, sys

from constants import *
from pygame import Color


def menu(screen):
    """
    Run the menu program.
    :returns: The character 'T', 'D', or 'F' in order to indicate which class was selected.
    :param screen: The screen of the pygame instance
    """

    ### INTIALIZE FONTS AND COLOURS ###

    # Get Consolas at size 48
    font = pygame.font.SysFont("Consolas", 48)

    # Get Consolas at a quarter the window height
    titleFont = pygame.font.SysFont("Consolas", HEIGHT // 3)

    # Colour scheme generated with https://coolors.co/   
    backDarkC = Color("#594236")
    titleC = Color("#48acf0")
    subtitleC = Color("#ff9b21")
    selectedC = Color("#6f584b")

    # Define the margin from the top and corner in pixels
    offset = 5

    # Character select loop
    characterSelected = False

    while not characterSelected:

        pygame.time.Clock().tick(75)

        # Get the mouse posittion and calculate the quarter of the screen
        #  which it is on

        locX = pygame.mouse.get_pos()[0]
        selectedBox = int(4 * locX / WIDTH)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the close button is pressed, exit the program
                sys.exit()

            # If the screen is clicked, determine if and which character was selected
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (selectedBox == 1):
                    playerType = "T"
                    characterSelected = True
                elif (selectedBox == 2):
                    playerType = "D"
                    characterSelected = True
                elif (selectedBox == 3):
                    playerType = "F"
                    characterSelected = True

        # TODO: draw UI so that the user knows what they are picking

        # Fill background with dark
        screen.fill(backDarkC)

        # Highlight the quarter that is being hovered over
        if (selectedBox > 0):
            # Get a subsurface representing the quarter
            surfaceSelected = screen.subsurface(pygame.Rect(selectedBox * WIDTH // 4, 0, WIDTH // 4, HEIGHT))
            surfaceSelected.fill(selectedC)

        # Draw box around the title
        # TODO:

        # Draw the title of the game
        screen.blit(titleFont.render("4", False, titleC),
                    pygame.Rect(offset + 15, offset,0,0)) # This is shifted over a bit to look better
        screen.blit(titleFont.render("C", False, titleC),
                    pygame.Rect(offset, offset + titleFont.get_height(),0,0))
        screen.blit(titleFont.render("L", False, titleC),
                    pygame.Rect(offset + 5, offset + 2 * titleFont.get_height(),0,0))

        # Draw the text that says each classes name
        screen.blit(font.render("Threemason", False, subtitleC),
                    pygame.Rect(1 * WIDTH // 4 + offset,offset,0,0))
        screen.blit(font.render("Dialic", False, subtitleC),
                    pygame.Rect(2 * WIDTH // 4 + offset,offset,0,0))
        screen.blit(font.render("Foursealer", False, subtitleC),
                    pygame.Rect(3 * WIDTH // 4 + offset,offset,0,0))

        pygame.display.flip()

    return playerType