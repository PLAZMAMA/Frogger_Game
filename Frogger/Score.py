import pygame
from Text import Text

class Score(Text):
    def __init__(self, display):
        super().__init__(display,"",30,(0,0,255),1,1)
        self.reset_score()

    def add_score(self):
        self.streak += 1
        self.score = "score: " + str(self.streak)
        self.surface = self.font.render(self.score, True, self.color)

    def reset_score(self):
        self.streak = 0
        self.score = "score: " + str(self.streak)
        self.surface = self.font.render(self.score, True, self.color)
