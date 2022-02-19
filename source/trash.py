import pygame

from source.spritesheet import Spritesheet
from source.settings import TRASH_SPRITESHEET_PATH
from source.settings import MIN_TRASH_SPEED_UNTIL_STATIONARY
from source.settings import TRASH_SLOWDOWN_RATE


class Trash:
    def __init__(self, initial_pos, initial_velocity, mass, player):
        self.pos = pygame.Vector2(initial_pos[0], initial_pos[1])
        self.velocity = pygame.Vector2(initial_velocity[0], initial_velocity[1])
        self.mass = mass
        # TODO: FINISH OFF TRASH MOVEMENT USING THE TRASH MOVEMENT CLASS
        self.sprite = Spritesheet(TRASH_SPRITESHEET_PATH, 1, 1)

    def get_mass(self):
        return self.mass

    def update(self, screen):
        # If the velocity of the trash is below a certain threshold, it will come to a stop
        if self.velocity.magnitude() > MIN_TRASH_SPEED_UNTIL_STATIONARY:
            self.pos += self.velocity

        # Diminish the velocity so slow down the trash item
        self.velocity *= TRASH_SLOWDOWN_RATE

        self.sprite.draw(screen, self.pos)
