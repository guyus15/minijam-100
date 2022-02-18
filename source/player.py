from turtle import Screen
import pygame
<<<<<<< HEAD
from settings import *
=======

from source.spritesheet import Spritesheet
>>>>>>> 3daaeb53a8f9b144abe33c224e5614c3987f0dbc

class Player(pygame.sprite.Sprite):
    def __init__(self, initial_pos):
        super().__init__()
        self.pos = pygame.Vector2(initial_pos)
        self.player_size = (64, 64)  # Setting player size to be changed through upgrades
        self.player_speed = 10
        self.sprite = Spritesheet("resources/test-image.png", 1, 4)

<<<<<<< HEAD
        self.image = pygame.Surface((self.player_size))
        self.image.fill(BLACK)        
        self.rect = self.image.get_rect()

    
    def player_movement(self):
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_a] and self.rect.x >= 0 or keys_pressed[pygame.K_LEFT] and self.rect.x >= 0: #Left
            self.rect.x -= self.player_speed
        if keys_pressed[pygame.K_d] and self.rect.x <= SCREEN_WIDTH - self.player_size[0] or keys_pressed[pygame.K_RIGHT] and self.rect.x <= SCREEN_WIDTH - self.player_size[0]: #Right
            self.rect.x += self.player_speed
        if keys_pressed[pygame.K_w] and self.rect.y >= 0 or keys_pressed[pygame.K_UP] and self.rect.y >= 0: #Up
            self.rect.y -= self.player_speed
        if keys_pressed[pygame.K_s] and self.rect.y <= SCREEN_HEIGHT - self.player_size[1] or keys_pressed[pygame.K_DOWN] and self.rect.y <= SCREEN_HEIGHT - self.player_size[1]: #Down
            self.rect.y += self.player_speed
=======
    def player_movement(self):
        keys_pressed = pygame.key.get_pressed()
>>>>>>> 3daaeb53a8f9b144abe33c224e5614c3987f0dbc

        if keys_pressed[pygame.K_a] and self.pos.x >= 0 or keys_pressed[pygame.K_LEFT] and self.pos.x >= 0:  # Left
            self.pos.x -= self.player_speed
        if keys_pressed[pygame.K_d] and self.pos.x <= 800 - self.player_size[0] or keys_pressed[
            pygame.K_RIGHT] and self.pos.x <= 800 - self.player_size[0]:  # Right
            self.pos.x += self.player_speed
        if keys_pressed[pygame.K_w] and self.pos.y >= 0 or keys_pressed[pygame.K_UP] and self.pos.y >= 0:  # Up
            self.pos.y -= self.player_speed
        if keys_pressed[pygame.K_s] and self.pos.y <= 500 - self.player_size[1] or keys_pressed[
            pygame.K_DOWN] and self.pos.y <= 500 - self.player_size[1]:  # Down
            self.pos.y += self.player_speed

    def update(self, screen):
        self.player_movement()
        self.sprite.draw(screen, self.pos)
        self.sprite.next_frame()

