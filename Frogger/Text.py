import pygame

class Text():
    def __init__(self,display,content,size,color = (255,0,0), locationX = 0, locationY = 0):
        self.x = locationX
        self.y = locationY
        self.display = display
        self.Dinfo = pygame.display.Info()
        self.text = content
        self.color = color
        self.font = pygame.font.Font(None,size)
        self.surface = self.font.render(self.text, True, self.color)
        self.size = self.font.size(self.text)
        if self.x == 0:
            self.x = int((self.Dinfo.current_w - self.size[0])/2)
        if self.y == 0:
            self.y = int((self.Dinfo.current_h - self.size[1])/2)

    def show(self):
        self.display.blit(self.surface,(self.x,self.y))