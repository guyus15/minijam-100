import pygame
import random

from source.spritesheet import Spritesheet
from source.movement import TrashMovement
from source.vector import Vector
from source.settings import TRASH_SPRITESHEET_PATH
from source.settings import TRASH_DISTANCE_TO_SUCK
from source.settings import TRASH_COLLECT_SPEED
from source.settings import TRASH_DISTANCE_TO_DELETE


class Trash:
    def __init__(self, initial_pos, initial_velocity, rotation, mass, player):
        self.pos = Vector(initial_pos.x, initial_pos.y)
        self.velocity = Vector(initial_velocity.x, initial_velocity.y)
        self.rotation = rotation
        self.mass = mass
        self.movement = TrashMovement(TRASH_COLLECT_SPEED, self.pos, self.velocity, target=player.get_pos())
        self.collision_rect = pygame.Rect((self.pos.x, self.pos.y), (128,128))
        self.sprite = Spritesheet(TRASH_SPRITESHEET_PATH, 2, 3)
        self.random_frame = random.randint(1, 6)
        self.should_play_sucking_sound = False
        self.should_delete = False
        self.found_sprite = False

    def get_mass(self):
        return self.mass

    def should_remove_from_trash(self):
        return self.should_delete

    def update(self, screen):

        distance_from_target = self.movement.get_distance_to_target()

        if distance_from_target <= TRASH_DISTANCE_TO_SUCK:
            # Update the trash items movement to move towards the player
            self.movement.move_towards_target()

            if self.should_play_sucking_sound:
                suck_sound = pygame.mixer.Sound("resources/suck.wav")
                # suck_sound.play()
                self.should_play_sucking_sound = False

            # Delete the object and increment the total mass if the distance to the player is below a set threshold
            if distance_from_target <= TRASH_DISTANCE_TO_DELETE:
                self.should_delete = True
        else:
            # Reset sucking sound
            self.should_play_sucking_sound = True

        self.movement.update()
        self.pos = self.movement.get_pos()

        self.collision_rect = pygame.Rect((self.pos.x, self.pos.y), (128, 128))

        if not self.found_sprite:
            for i in range(0, self.random_frame):
                self.sprite.next_frame()

            self.found_sprite = True

        self.sprite.draw(screen, self.pos, rotation=self.rotation, size=(128, 128))
