import pygame

from source.spritesheet import Spritesheet
from source.settings import TRASH_SPRITESHEET_PATH


class Trash:
    def __init__(self, initial_pos, initial_velocity, mass):
        self.pos = pygame.Vector2(initial_pos[0], initial_pos[1])
        self.velocity = pygame.Vector2(initial_velocity[0], initial_velocity[1])
        self.mass = mass
        self.sprite = Spritesheet(TRASH_SPRITESHEET_PATH, 1, 1)

    def get_mass(self):
        return self.mass

    def update(self, screen):
        self.pos += self.velocity
        self.sprite.draw(screen, self.pos)
