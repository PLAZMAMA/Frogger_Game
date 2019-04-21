import pygame
from Game_object import Game_object
import random

class Path(Game_object):
    def __init__(self,display,imagefile,locationY,Hspeed,path_height):
        self.Dinfo = pygame.display.Info()
        self.width = int(self.Dinfo.current_w)
        self.height = path_height
        super().__init__(display,imagefile,self.width,self.height,0,locationY)
        self.direction = random.randint(0,1)
        if self.direction == 0:
            self.direction = -1
        self.Hspeed = Hspeed * self.direction
        if self.direction == -1:
            self.I = random.randint(50,150)
        else:
            self.I = self.width - random.randint(50,150)
        self.Objects = []

    def add_objects(self):
        r_num = random.randint(10,15)
        for _ in range(r_num):
            Object = self.add_object()
            Object.y = self.y + (self.height-Object.height)/2
            if self.direction == -1:
                Object.x = self.I
                self.I += Object.width + random.randint(int(self.Dinfo.current_w/8),int(self.Dinfo.current_w/4))
            else:
                Object.x = self.I - Object.width
                self.I -= Object.width + random.randint(int(self.Dinfo.current_w/8),int(self.Dinfo.current_w/4))
            self.Objects.append(Object)

    def traffic(self,Player):
        if self.direction == -1:
            for Object in self.Objects:
                if Object.x + Object.width < 0:
                    Object.x = self.I
                    self.I += Object.width + random.randint(int(self.Dinfo.current_w/8),int(self.Dinfo.current_w/4))
                else:
                    Object.move(self.Hspeed,0)
        else:
            for Object in self.Objects:
                if Object.x > self.width:
                    Object.x = self.I - Object.width
                    self.I -= random.randint(int(self.Dinfo.current_w/8),int(self.Dinfo.current_w/4))
                else:
                    Object.move(self.Hspeed,0)

    def on_objects(self,Player):
        if self.player_on_path(Player):
            for Object in self.Objects:
                if Object.check_on(Player):
                    return True
        return False

    def player_on_path(self,Player):
        if Player.y <= (self.y + self.height) and (Player.y + Player.height) >= self.y:
            return True
        return False

    def show(self):
        super().show()
        for Object in self.Objects:
            Object.show()
