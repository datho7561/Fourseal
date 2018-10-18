from pygame import Surface
from pygame import Color
from pygame import Rect
from entity import Entity

class DamageBar:

    LIFE_COLOUR = Color(102, 255, 51, 255)
    DEATH_COLOUR = Color(102, 0, 0, 255)

    def __init__(self,
                 x,
                 y, 
                 height=10, # How tall the box is (width is computed from this)
                 colour1=Color(102, 255, 51, 255), # Life colour
                 colour2=Color(102, 0, 0, 255)): # Death colour

        # The size of the health bar
        self.width = height * 8
        self.height = height

        # The colours to use for the health bar
        self.colour1 = colour1
        self.colour2 = colour2

        # Position of health bar on screen
        self.x = x
        self.y = y

        # The image representation of the health bar
        self.bar = Surface((self.width, self.height))

        # A fraction that represents how much life this thing has left
        self.fraction = 1.0

    def update(self, value):

        if (isinstance(value, Entity)):
            self.fraction = value.health / value.maxHealth
        else:
            self.fraction = value
        
        # Fraction should be at most 1
        if (self.fraction > 1):
            self.fraction = 1

    def draw(self, other):

        # TODO: make border less sloppy and more parameter based
        # currently it is 2 pixels thick all around

        # Outside border
        self.bar.fill(Color("black"))

        # Fill the inside with the empty colour
        toFillPart = self.bar.subsurface(Rect(2, 2, self.width-4, self.height-4))
        toFillPart.fill(self.colour2)

        # Cover up part of it with the 'life' colour
        filledPart = toFillPart.subsurface(Rect(0, 0, int((self.width - 4) * self.fraction), self.height - 4))
        filledPart.fill(self.colour1)

        other.blit(self.bar, (self.x, self.y))
