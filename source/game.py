# Import and initialize the pygame library

import pygame
from source.player import *
from source.settings import *


class Game:

    def __init__(self):
        pygame.init()
        self.screen = None
        self.window_setup()
        self.clock = pygame.time.Clock()
        self.player = Player((SCREEN_WIDTH / 2 - 32, SCREEN_HEIGHT / 2 - 32))

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Mini Jam Game")
        self.screen.fill(WHITE)

    def update(self):
        self.screen.fill(WHITE)
        self.player.update(self.screen)  # Updates player behaviour

    def play_game(self):
        running = True

        while running:
            self.clock.tick(FPS)  # Sets game FPS

            for event in pygame.event.get():  # Checking for the user pressing the window close button
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:  # Checking for Space key (size_up)
                    if event.key == pygame.K_p:
                        self.player.upgrade(size_up=True)
                if event.type == pygame.KEYDOWN:  # Checking for Space key (size_up)
                    if event.key == pygame.K_o:
                        self.player.upgrade(speed_up=True)

            self.update()
            pygame.display.update()

        pygame.quit()  # Quit the game once running == False
