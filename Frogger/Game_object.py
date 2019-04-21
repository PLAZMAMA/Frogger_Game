import pygame

class Game_object():
    def  __init__(self,display,imagefile,width,height,locationX,locationY):
        image = pygame.image.load(imagefile)
        self.image = pygame.transform.scale(image,(width,height))
        self.width = width
        self.height = height
        self.x = locationX
        self.y = locationY
        self.display = display
        self.Dinfo = pygame.display.Info()
       
    def show(self):
        self.display.blit(self.image,(self.x,self.y))

    def right(self,Hspeed):
        if (self.x+self.width+Hspeed) <= self.Dinfo.current_w:
            self.x += Hspeed

    def left(self,Hspeed):
        if(self.x - Hspeed) >= 0:
            self.x -= Hspeed

    def up(self,Vspeed):
        if(self.y - Vspeed) >= 0:
            self.y -= Vspeed

    def down(self,Vspeed):
        if (self.y + self.height + Vspeed) <= self.Dinfo.current_h:
            self.y += Vspeed

    def move(self,x,y):
        self.x += x
        self.y += y
    
    def check_on(self,Player):
        if ((Player.x + Player.width) >= self.x) and (Player.x <= (self.x + self.width)):
            return True
        return False 
