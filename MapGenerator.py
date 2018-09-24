import random
from constants import *

file = open("NewRandomMap", 'w')

text = ""

# FULL RANDOM BACKGROUND
for row in range (BOXES_HIGH):
    for col in range(BOXES_WIDE):
        text += str(random.randrange(1, 9))
        if col!=BOXES_WIDE-1:
            text+=", "
    text+='\n'

# FULL RANDOM FOREGROUND
#for row in range (BOXES_HIGH):
#    for col in range(BOXES_WIDE):
#        text += str(random.randrange(9, 16) * random.randrange(0, 2))
#        if col!=BOXES_WIDE-1:
#            text+=", "
#    text+='\n'

# RANDOM OUTLINE FOREGROUND
for row in range (BOXES_HIGH):
    for col in range(BOXES_WIDE):
        if row == 0 or row == BOXES_HIGH-1 or col == 0 or col == BOXES_WIDE-1:
            text += str(random.randrange(9, 16))
        else:
            text += str(0)
        if col!=BOXES_WIDE-1:
            text+=", "
    text+='\n'

file.write(text)

file.close()
