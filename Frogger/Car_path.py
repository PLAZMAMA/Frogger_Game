import pygame
from Path import Path
import random
from Car import Car 
from Truck import Truck
from Bike import Bike

class Car_path(Path):
    CAR = 0
    TRUCK = 1
    BIKE = 2
    def __init__(self,display,locationY,Hspeed,path_height):
        super().__init__(display,"media/images/car_path.jpg",locationY,Hspeed,path_height)
        
    def add_object(self):
        vehicleType = random.randint(0,2)
        if vehicleType == self.CAR:
            Object = Car(self.display,int(self.width/10),self.height,0,0,self.Hspeed,self.direction)
        elif vehicleType == self.TRUCK:
            Object = Truck(self.display,int(self.width/5),self.height,0,0,self.Hspeed,self.direction)
        else:
            Object = Bike(self.display,int(self.width/10),self.height,0,0,self.Hspeed,self.direction)
        return Object

    def failed(self,Player):
        return self.on_objects(Player)