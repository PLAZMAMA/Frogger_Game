import pygame
from Car_path import Car_path
import random
from Paths import Paths

class Road(Paths):
    def __init__(self,display,locationY,Player,path_height):
        super().__init__(display,locationY,Player,path_height,pygame.mixer.Sound("media/sounds/crash.wav"))

    def build(self):
        num = random.randint(2,3)
        for i in range(num):
            path = Car_path(self.display,0, self.Dinfo.current_w / int(self.Dinfo.current_w/random.randint(3,5)),self.path_height)
            path.y = self.y + (i * path.height)
            path.add_objects()
            self.paths.append(path)