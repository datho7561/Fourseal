# Author: David Thompson
# Date: 13 April, 2018

# This module holds a lot of important game variables that must be accessed by multiple classes

global BOX_SIZE, BOXES_WIDE, BOXES_HIGH, WIDTH, HEIGHT, SIZE, ENEMY_TIME, RECOIL

# The width/height of a standard block
BOX_SIZE = 32

# Number of boxes horizontally and veritcally
BOXES_WIDE, BOXES_HIGH = 32, 18

# The size (width and height) of the window in pixels
SIZE = WIDTH, HEIGHT = BOX_SIZE*BOXES_WIDE, BOX_SIZE*BOXES_HIGH

# How fast the enemies spawn
ENEMY_TIME = 120

# How much entities get knocked back
RECOIL = 8
RECOIL_SPEED = 8