import random

import pygame

from source.trash import Trash
from source.vector import Vector
from source.time_manager import TimeManager
from source.settings import MIN_TRASH_SPEED
from source.settings import MAX_TRASH_SPEED
from source.settings import MIN_TRASH_MASS
from source.settings import MAX_TRASH_MASS
from source.settings import MAX_TRASH_PER_SPAWNER
from source.settings import TRASH_SPAWN_PERIOD


class TrashSpawner:
    def __init__(self, pos, direction, player):
        self.pos = pos
        self.direction = direction
        self.player = player
        self.spawned_trash = []
        self.total_spawned = 0
        self.total_sucked = 0
        self.possible_directions_from_bottom = [(1, 1), (0.5, 1), (0, 1), (-0.5, 1), (-1, 1)]

    def spawn(self):

        # If the trash spawner has reach the max amount of items it can spawn, exit
        if len(self.spawned_trash) >= MAX_TRASH_PER_SPAWNER:
            return

        # Pick a random velocity for the trash to be thrown at

        random_direction = random.choice(self.possible_directions_from_bottom)

        vector = Vector(random_direction[0], random_direction[1])

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

        vector.multiply(random_speed)

        new_trash_item = Trash(self.pos, vector, random_mass, self.player)

        self.spawned_trash.append(new_trash_item)
        self.total_spawned += 1

    def get_current_trash(self):
        return self.spawned_trash

    def update(self, screen):
        if TimeManager.transition(TRASH_SPAWN_PERIOD):
            self.spawn()

        for trash_item in self.spawned_trash:
            trash_item.update(screen)
            if trash_item.should_remove_from_trash() and self.player.can_add_item():
                self.spawned_trash.remove(trash_item)
                self.player.add_trash_item(trash_item)
                sound = pygame.mixer.Sound("resources/pop.wav")
                sound.play()
                self.total_sucked += 1


