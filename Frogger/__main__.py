import pygame
import FroggerGame

if __name__=="__main__":
    pygame.init()
    game = FroggerGame.FroggerGame(1280,900)
    game.run()