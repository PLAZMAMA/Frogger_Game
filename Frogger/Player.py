import pygame
import random
from Game_object import Game_object

class Player(Game_object):
    def __init__(self,display,path_height):
        self.Dinfo = pygame.display.Info()
        self.path_height = path_height
        self.Hspeed = int(self.path_height/2)
        self.Vspeed = self.path_height
        self.width = self.path_height-10
        self.height = self.path_height-10
        self.start_y = self.starting_y()       
        self.reset()
        super().__init__(display,"media/images/chicken.png",self.width,self.height,self.x,self.y)
        self.r_image = pygame.transform.rotate(self.image,-90)
        self.l_image = pygame.transform.rotate(self.image,90)
        self.u_image = self.image
        self.d_image = pygame.transform.rotate(self.image,180)
        self.sounds = [pygame.mixer.Sound("media/sounds/Chicken1.wav"), pygame.mixer.Sound("media/sounds/Chicken2.wav"), pygame.mixer.Sound("media/sounds/Chicken3.wav")]

    def play_sound(self):
        pygame.mixer.Sound.play(self.sounds[random.randint(0,len(self.sounds)-1)])

        

    def movement(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and self.x < (self.Dinfo.current_w - self.width):
                self.play_sound()
                self.image = self.r_image
                self.x += self.Hspeed
            elif event.key == pygame.K_LEFT and self.x > 0:
                self.play_sound()
                self.image = self.l_image
                self.x -= self.Hspeed
            elif event.key == pygame.K_UP:
                self.play_sound()
                self.image = self.u_image
                self.y -= self.Vspeed
            elif event.key == pygame.K_DOWN and self.y < self.start_y:
                self.play_sound()
                self.image = self.d_image
                self.y += self.Vspeed

    def reset(self):
        self.y = self.start_y
        self.x = int((self.Dinfo.current_w - self.width)/2)

    def starting_y(self):
        ah = self.Dinfo.current_h -(self.Dinfo.current_h % self.path_height)
        return (ah - self.path_height) + int((self.path_height-self.height)/2)

    def player_won(self):
        return self.y < self.path_height