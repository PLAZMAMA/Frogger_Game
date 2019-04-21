import pygame
from Log_path import Log_path
import random
from Paths import Paths

class River(Paths):
    def __init__(self,display,locationY,Player,path_height):
        super().__init__(display,locationY,Player,path_height,pygame.mixer.Sound("media/sounds/splash.wav"))

    def build(self):
        num = random.randint(2,3)
        for i in range(num):
            path = Log_path(self.display,0,self.Dinfo.current_w / int(self.Dinfo.current_w/random.randint(3,5)),self.path_height)
            path.y = self.y + (i * path.height)
            path.add_objects()
            self.paths.append(path)