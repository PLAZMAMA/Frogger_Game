import pygame
from Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self,display,width,height,locationX,locationY,Hspeed,direction):
        super().__init__(display,"media/images/truck.png",width,height,locationX,locationY,Hspeed,direction)