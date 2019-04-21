import pygame
from Path import Path
import random
from Log import Log

class Log_path(Path):
    def __init__(self,display,locationY,Hspeed,path_height):
        super().__init__(display,"media/images/log_path.jpg",locationY,Hspeed,path_height)

    def add_object(self):
        log = Log(self.display,0,0,self.height)
        return log

    def traffic(self,Player):
        super().traffic(Player)
        if self.on_objects(Player):
            Player.move(self.Hspeed,0)


    def failed(self,Player):
        if self.player_on_path(Player) and not self.on_objects(Player):
            return True
        return False