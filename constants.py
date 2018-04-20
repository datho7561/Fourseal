# Author: David Thompson
# Date: 13 April, 2018

# This module holds a lot of important game variables that must be accessed by multiple classes

global BOX_SIZE, BOXES_WIDE, BOXES_HIGH, WIDTH, HEIGHT, SIZE

# The width/height of a standard block
BOX_SIZE = 32

# Number of boxes horizontally and veritcally
BOXES_WIDE, BOXES_HIGH = 32, 18

# The size (width and height) of the window in pixels
SIZE = WIDTH, HEIGHT = BOX_SIZE*BOXES_WIDE, BOX_SIZE*BOXES_HIGH
