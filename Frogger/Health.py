import pygame
from Life import Life

class Health():
    def __init__(self,display,x=5,y=5):
        self.display = display
        self.Dinfo = pygame.display.Info()
        self.y = y
        if x==5:
            self.x = int(self.Dinfo.current_w * 0.75)
        else:
            self.x = x
        self.reset_health()

    def reset_health(self):
        self.health = []
        width = int(self.Dinfo.current_w/40)
        height = int(self.Dinfo.current_h/40)
        for i in range(3):
            self.health.append(Life(self.display,width,height,self.x+(i*width)+i,self.y))

    def loose_health(self):
        if len(self.health) > 1:
            del self.health[len(self.health)-1]
            return True
        else:
            return False

    def show(self):
        for life in self.health:
            life.show()