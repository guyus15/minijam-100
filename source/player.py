import pygame
from source.settings import *
from source.spritesheet import Spritesheet
from source.movement import Movement
from source.collider import PlayerCollider
from source.vector import Vector


class Player(pygame.sprite.Sprite):
    def __init__(self, initial_pos):
        super().__init__()
        self.pos = Vector(initial_pos[0], initial_pos[1])
        self.player_size = (64, 64)  # Setting player size to be changed through upgrades
        self.size_up_num = 0  # Number of size upgrades
        self.player_speed = 10
        self.speed_up_num = 0  # Number of movement speed upgrades

        self.movement = Movement(self.player_speed, self.pos)
        PlayerCollider.__init__(self, self.pos, self.movement, self.player_size)
        self.sprite = Spritesheet(PLAYER_SPRITESHEET_PATH, 1, 1)

    def player_movement(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a] and self.pos.x >= 0 or keys_pressed[pygame.K_LEFT] and self.pos.x >= 0:  # Left
            self.movement.move_horizontal(-1)
        if keys_pressed[pygame.K_d] and self.pos.x <= SCREEN_WIDTH - self.player_size[0] or keys_pressed[
            pygame.K_RIGHT] and self.pos.x <= SCREEN_WIDTH - self.player_size[0]:  # Right
            self.movement.move_horizontal(1)
        if keys_pressed[pygame.K_w] and self.pos.y >= 0 or keys_pressed[pygame.K_UP] and self.pos.y >= 0:  # Up
            self.movement.move_vertical(1)
        if keys_pressed[pygame.K_s] and self.pos.y <= SCREEN_HEIGHT - self.player_size[1] or keys_pressed[
            pygame.K_DOWN] and self.pos.y <= SCREEN_HEIGHT - self.player_size[1]:  # Down
            self.movement.move_vertical(-1)

        self.movement.update()

    def upgrade(self, size_up=False, speed_up=False):

        if size_up and self.size_up_num <= 4:
            self.player_size = (self.player_size[0] * 1.5, self.player_size[1] * 1.5)
            self.movement.set_speed(self.player_speed)
            self.size_up_num += 1
            print("Becoming Chip")

        if speed_up and self.speed_up_num <= 4:
            self.player_speed = (self.player_speed * 1.5)
            self.movement.set_speed(self.player_speed)
            self.speed_up_num += 1
            print("Becoming Fin")

    def get_pos(self):
        return self.pos

    def update(self, screen):
        self.player_movement()
        self.pos = self.movement.get_pos()
        self.sprite.draw(screen, self.pos, size=self.player_size, rotation=self.movement.get_rotation())
        self.sprite.next_frame()
