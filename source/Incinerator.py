import imp
import pygame
from settings import *
from spritesheet import *

class Incinerator(pygame.sprite.Sprite): 

    def __init__(self, pos):
        super().__init__()
        self.incin_size = 80, 90
        self.pos = pygame.Vector2(pos)
        self.incin_surface = pygame.Surface(self.incin_size)

    def detect_player(self):
        pass
    
    def incinerate(self):
        pass

    def update(self, screen):
        self.sprite.draw(screen, self.pos, size = self.incin_size)
        self.sprite.next_frame()
    
