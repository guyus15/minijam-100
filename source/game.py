# Import and initialize the pygame library

import pygame
from player import *
from settings import *

pygame.init()

# Set up the drawing window

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Mini Jam Game")
background_image = pygame.image.load('Mini Jam 100/minijam-100/resources/test-background.png')
background = pygame.transform.scale(background_image, SCREEN_SIZE)
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

    #screen.fill(WHITE)
    screen.blit(background,(0,0))
    # Handle player movement

    player.player_movement()
    player.update(screen)

    # Flip the display

    pygame.display.update()

# Quit the game
pygame.quit()

