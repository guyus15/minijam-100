import random
import pygame

from source.trash import Trash
from source.settings import *


class TrashSpawner:
    def __init__(self, pos, direction):
        self.pos = pos
        self.direction = direction
        self.spawned_trash = []
        self.total_spawned = 0
        self.possible_directions_from_bottom = [(1, 1), (0.5, 1), (0, 1), (-0.5, 1), (-1, 1)]

    def spawn(self):
        print("Spawning trash!")

        # Pick a random velocity for the trash to be thrown at

        random_direction = random.choice(self.possible_directions_from_bottom)

        vector = pygame.Vector2(random_direction[0], random_direction[1])

        # Determine which set of directions to give the spawner, it is facing upwards by default

        if self.direction[0] == 1:
            # Facing right
            vector = vector.rotate(-90)
        elif self.direction[0] == -1:
            # Facing left
            vector = vector.rotate(90)
        elif self.direction[1] == -1:
            # Facing down
            vector = vector.rotate(180)

        random_speed = random.randint(MIN_TRASH_SPEED, MAX_TRASH_SPEED)
        random_mass = random.randint(MIN_TRASH_MASS, MAX_TRASH_MASS)

        vector.scale_to_length(random_speed)

        new_trash_item = Trash(self.pos, vector, random_mass)

        self.spawned_trash.append(new_trash_item)

    def update(self, screen):
        for trash_item in self.spawned_trash:
            trash_item.update(screen)
