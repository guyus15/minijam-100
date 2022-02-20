import pygame

from source.vector import Vector
from source.spritesheet import Spritesheet
from source.time_manager import TimeManager
from source.settings import INCINERATOR_SPRITESHEET_PATH
from source.settings import INCINERATOR_SPEED


class Incinerator:
    def __init__(self, pos_vector, collision_area, player):
        self.pos = pos_vector
        self.collision_area = collision_area
        self.size = Vector(150, 150)
        self.collision_box = pygame.Rect((self.pos.x + 27, self.pos.y + 100), (self.collision_area.x, self.collision_area.y))
        self.total_incinerated_items = 0
        self.total_mass_incinerated = 0
        self.player = player

        self.spritesheet = Spritesheet(INCINERATOR_SPRITESHEET_PATH, 1, 1)

    def add_item(self, mass):
        self.total_incinerated_items += 1
        self.total_mass_incinerated += mass

    def player_in_area(self):
        return pygame.Rect.colliderect(self.collision_box, self.player.collision_box)

    def update(self, screen):
        if self.player_in_area() and TimeManager.transition(INCINERATOR_SPEED):
            self.player.remove_trash_item()

        pygame.draw.rect(screen, (255, 255, 255), self.collision_box, 5, 5, 5, 5)
        self.spritesheet.draw(screen, self.pos, size=(self.size.x, self.size.y))
