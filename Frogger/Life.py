import pygame
from Game_object import Game_object

class Life(Game_object):
    def __init__(self,display,width,height,locationX,locationY):
        super().__init__(display,"media/images/life.png",width,height,locationX,locationY)