# Import and initialize the pygame library

import pygame
from source.player import *
from source.settings import *

pygame.init()

# Set up the drawing window

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Mini Jam Game")

player = Player()

clock = pygame.time.Clock()

# Run until the user asks to quit

running = True
while running:

    clock.tick(FPS)

    # Checking for the user pressing the window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Handle player movement

    player.player_movement()
    player.update(screen)

    # Flip the display

    pygame.display.update()

# Quit the game
pygame.quit()
