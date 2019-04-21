import pygame
import random

class Paths():
    def __init__(self,display,locationY,Player,path_height,c_sound):
        self.c_sound = c_sound
        self.display = display
        self.Dinfo = pygame.display.Info()
        self.y = locationY
        self.paths = []
        self.path_height = path_height
        self.build()
        self.height = self.paths[0].height * len(self.paths)

    def build(self):
        pass
        
    def check_on(self,Player):
        if Player.y <= (self.y + self.height) and (Player.y + Player.height) >= self.y:
            return True
        return False

    def show(self):
        for path in self.paths:
            path.show()

    def failed(self,Player):
        for path in self.paths:
            if path.failed(Player):
                return True
        return False

    def traffic(self,Player):
        for path in self.paths:
            path.traffic(Player)