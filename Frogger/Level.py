import pygame
import random
from River import River
from Road import Road

class Level():
    def __init__(self,display,Player,path_height):
        self.display = display
        self.Dinfo = pygame.display.Info()
        self.y = 0
        self.height = 0
        self.player = Player
        self.paths = []
        self.path_height = path_height
        self.build(display)
        

    def build(self,display):
        path = ""
        while self.height + self.path_height < self.Dinfo.current_h:
            r_num = random.randint(0,2)
            if r_num  <= 1:
               path = Road(display,self.path_height+self.height,self.player,self.path_height)
            else:
                path  = River(display,self.path_height+self.height,self.player,self.path_height)

            if self.height + path.height + self.path_height < self.Dinfo.current_h:
                self.paths.append(path)
                self.height = path.y + path.height
            else:
                break

    def failed(self,Player):
        for path in self.paths:
            if path.failed(self.player):
                pygame.mixer.Sound.play(path.c_sound)
                return True
        return False
    
    def show(self):
        for path in self.paths:
            path.show()

    def traffic(self,Player):
        for path in self.paths:
            path.traffic(Player)