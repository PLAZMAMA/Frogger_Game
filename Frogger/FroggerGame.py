import pygame
from Game_object import Game_object
from Player import Player
from Path import Path
from Level import Level
from Health import Health
from Text import Text
from Score import Score
import time

class FroggerGame():
    def __init__(self,displaywidth,displayheight):
        self.white=(255,255,255)
        self.black=(0,0,0)
        self.red=(255,0,0)
        self.green=(0,255,0)
        self.blue=(0,0,255)
        self.width=displaywidth
        self.height=displayheight
        self.path_height = int(self.height/15)
        self.screen=pygame.display.set_mode((self.width,self.height))
        bgimage = pygame.image.load("media/images/grassy_area.jpg").convert()
        self.backgroundImage = pygame.transform.scale(bgimage, (self.width,self.height))
        lostImage = pygame.image.load("media/images/wasted.png")
        self.lost_image = pygame.transform.scale(lostImage, (self.width,self.height))
        self.player = Player(self.screen,self.path_height)
        self.level = Level(self.screen,self.player,self.path_height)
        self.health = Health(self.screen)
        self.score = Score(self.screen)
        self.w_sound = pygame.mixer.Sound("media/sounds/YouWon.wav")
        self.l_sound = pygame.mixer.Sound("media/sounds/chickens.wav")
        pygame.display.set_caption("Frogger")

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            self.player.movement(event)

    def clean_events(self):
        for event in pygame.event.get():
            pass

    def completed_level(self,Player):
        if Player.y <= 0:
            return True
        return False

    def show(self):
        self.screen.blit(self.backgroundImage,(0,0))
        self.level.show()
        self.player.show()
        self.health.show()
        self.score.show()
        pygame.display.update()

    def creat_text(self,text,color = (255,0,0),locationX = 0,locationY = 0):
            text = Text(self.screen, text, 80, color, locationX, locationY)
            text.show()
            pygame.display.update()
            return (text)

    def reset_game(self):
        self.screen.blit(self.lost_image,(0,0))
        self.instruction = self.creat_text("(press space to play again)",(255,0,0),0,self.height -80)
        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.health.reset_health()
                    self.score.reset_score()
                    self.player.reset()
                    self.level = Level(self.screen,self.player, self.path_height)
                    self.player.image = self.player.u_image
                    wait = False

    def run(self):
        while True:
            self.event()
            self.show()
            self.level.traffic(self.player)
            if self.level.failed(self.player):
                pygame.mixer.Sound.play(self.l_sound)
                if not self.health.loose_health():
                    self.reset_game()
                else:
                    time.sleep(1)
                    self.player.reset()
                    self.level = Level(self.screen,self.player, self.path_height)
                    self.clean_events()
                    self.player.image = self.player.u_image
                pygame.mixer.Sound.stop(self.l_sound)
            if self.player.player_won():
                self.score.add_score()
                self.creat_text("Level completed!",(0,255,0))
                pygame.mixer.Sound.play(self.w_sound)
                time.sleep(1)
                self.player.reset()
                self.level = Level(self.screen,self.player, self.path_height)
                self.player.image = self.player.u_image