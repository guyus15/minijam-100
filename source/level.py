import pygame

from source.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Level:
    def __init__(self):
        self.collision_rects = []

        top_wall = pygame.Rect((0, 0), (SCREEN_WIDTH, 20))
        bottom_wall = pygame.Rect((0, SCREEN_HEIGHT - 20), (SCREEN_WIDTH, 20))
        left_wall = pygame.Rect((0, 0), (20, SCREEN_HEIGHT))
        right_wall = pygame.Rect((SCREEN_WIDTH - 20, 0), (20, SCREEN_HEIGHT))

        self.collision_rects.append(top_wall)
        #self.colliders.append(bottom_wall)
        self.collision_rects.append(left_wall)
        self.collision_rects.append(right_wall)

    def get_colliders(self):
        return self.collision_rects
