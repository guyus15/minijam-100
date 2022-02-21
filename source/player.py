import pygame
from source.spritesheet import Spritesheet
from source.movement import Movement
from source.vector import Vector
from source.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from source.settings import PLAYER_SPRITESHEET_PATH
from source.settings import MASS_BAR_X, MASS_BAR_Y, MASS_BAR_WIDTH, MASS_BAR_HEIGHT, PLAYER_MAX_MASS
from source.settings import INCINERATOR_SOUND_PATH


class Player(pygame.sprite.Sprite):
    def __init__(self, initial_pos):
        super().__init__()
        self.pos = Vector(initial_pos[0], initial_pos[1])
        self.player_size = (96, 96)  # Setting player size to be changed through upgrades
        self.collision_box = pygame.Rect((self.pos.x, self.pos.y), (self.player_size[0], self.player_size[0]))

        self.player_speed = 10

        # Upgrades
        self.speed_up_num = 0  # Number of movement speed upgrades
        self.size_up_num = 0  # Number of size upgrades

        self.movement = Movement(self.player_speed, self.pos)
        self.sprite = Spritesheet(PLAYER_SPRITESHEET_PATH, 1, 1)

        self.current_trash_item_mass = 0
        self.current_mass_incinerated = 0
        self.trash_items = []

        # Mass bar
        self.mass_bar_background = pygame.Rect((MASS_BAR_X, MASS_BAR_Y), (MASS_BAR_WIDTH, MASS_BAR_HEIGHT))
        self.mass_bar_foreground = pygame.Rect((MASS_BAR_X, MASS_BAR_Y), (0, MASS_BAR_HEIGHT))

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

    def can_add_item(self):
        return self.current_trash_item_mass <= PLAYER_MAX_MASS

    def add_trash_item(self, trash_item):
        self.trash_items.append(trash_item)
        self.current_trash_item_mass += trash_item.get_mass()

    def remove_trash_item(self):
        if len(self.trash_items):
            trash_item = self.trash_items.pop()
            self.current_trash_item_mass -= trash_item.get_mass()
            self.current_mass_incinerated += trash_item.get_mass()
            incinerator_sound = pygame.mixer.Sound(INCINERATOR_SOUND_PATH)
            incinerator_sound.play()

    def get_mass_incinerated(self):
        return self.current_mass_incinerated

    def upgrade(self, size_up=False, speed_up=False):

        if size_up and self.size_up_num <= 4:
            self.player_size = (self.player_size[0] * 1.5, self.player_size[1] * 1.5)
            self.movement.set_speed(self.player_speed)
            self.size_up_num += 1

        if speed_up and self.speed_up_num <= 4:
            self.player_speed = (self.player_speed * 1.5)
            self.movement.set_speed(self.player_speed)
            self.speed_up_num += 1

    def get_pos(self):
        return self.pos

    def update(self, screen):
        self.player_movement()
        self.pos = self.movement.get_pos()

        # Update the player's collision box
        self.collision_box.x = self.pos.x
        self.collision_box.y = self.pos.y

        # Update the player's mass bar
        mass_ratio = self.current_trash_item_mass / PLAYER_MAX_MASS
        self.mass_bar_foreground.width = mass_ratio * MASS_BAR_WIDTH

        # Draw the player
        self.sprite.draw(screen, self.pos, size=self.player_size, rotation=self.movement.get_rotation())
        self.sprite.next_frame()

        # Draw the mass bar
        pygame.draw.rect(screen, "black", self.mass_bar_background)
        pygame.draw.rect(screen, "green", self.mass_bar_foreground)
