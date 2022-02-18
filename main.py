# Import and initialize the pygame library

import pygame
from source.player import *
from source.settings import *

pygame.init()

# Set up the drawing window

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Mini Jam Game")

player = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

clock = pygame.time.Clock()

# Run until the user asks to quit

running = True

# This method will be called once per frame
def update():
    screen.fill(WHITE)

    # Handle player movement
    player.update(screen)

    pygame.display.update()
    clock.tick(FPS)


while running:
    # Checking for the user pressing the window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()

# Quit the game
pygame.quit()
