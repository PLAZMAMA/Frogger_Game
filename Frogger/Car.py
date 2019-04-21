import pygame
from Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self,display,width,height,locationX,locationY,Hspeed,direction):
        super().__init__(display,"media/images/car.png",width,height,locationX,locationY,Hspeed,direction)
       