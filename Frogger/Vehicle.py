import pygame
import random
from Game_object import Game_object

class Vehicle(Game_object):
    def __init__(self,display,imagefile,width,height,locationX,locationY,Hspeed,direction):
       super().__init__(display,imagefile,width,height,locationX,locationY)
       self.direction = direction
       self.flip()

    def flip(self):
        if self.direction == -1:
            self.image = pygame.transform.flip(self.image,True,False)
