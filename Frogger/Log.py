import pygame
import random
from Game_object import Game_object

class Log(Game_object):
    def __init__(self,display,locationX,locationY,height=0):
        width = random.randint(60,150)
        super().__init__(display,"media/images/log.png",width,height,locationX,locationY)
        