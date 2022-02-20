import pygame

from source.spritesheet import Spritesheet
from source.movement import TrashMovement
from source.vector import Vector
from source.settings import TRASH_SPRITESHEET_PATH
from source.settings import TRASH_DISTANCE_TO_SUCK
from source.settings import TRASH_COLLECT_SPEED
from source.settings import TRASH_DISTANCE_TO_DELETE


class Trash:
    def __init__(self, initial_pos, initial_velocity, mass, player):
        self.pos = Vector(initial_pos.x, initial_pos.y)
        self.velocity = Vector(initial_velocity.x, initial_velocity.y)
        self.mass = mass
        self.movement = TrashMovement(TRASH_COLLECT_SPEED, self.pos, self.velocity, target=player.get_pos())
        self.collision_rect = pygame.Rect((self.pos.x, self.pos.y), (64, 64))
        self.sprite = Spritesheet(TRASH_SPRITESHEET_PATH, 1, 1)
        self.should_move = True
        self.should_delete = False

    def get_mass(self):
        return self.mass

    def should_remove_from_trash(self):
        return self.should_delete

    def update(self, screen):

        distance_from_target = self.movement.get_distance_to_target()

        if distance_from_target <= TRASH_DISTANCE_TO_SUCK:
            # Update the trash items movement to move towards the player
            self.movement.move_towards_target()

            # Delete the object and increment the total mass if the distance to the player is below a set threshold
            if distance_from_target <= TRASH_DISTANCE_TO_DELETE:
                self.should_delete = True

        self.movement.update()
        self.pos = self.movement.get_pos()

        self.collision_rect = pygame.Rect((self.pos.x, self.pos.y), (64, 64))
        self.sprite.draw(screen, self.pos)
