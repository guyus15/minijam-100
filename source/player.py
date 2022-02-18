from turtle import Screen
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_size = (64,64) # Setting player size to be changed through upgrades
        self.player_speed = 10 # Same as above

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

    def update(self,screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))
        
    