import pygame
from Vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self,display,width,height,locationX,locationY,Hspeed,direction):
        super().__init__(display,"media/images/bike.png",width,height,locationX,locationY,Hspeed,direction)