# Import and initialize the pygame library

import pygame
from source.player import *
from source.settings import *
from source.trash_spawner import TrashSpawner

pygame.init()

# Set up the drawing window

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Mini Jam Game")

player = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

clock = pygame.time.Clock()

trash_spawner = TrashSpawner((SCREEN_WIDTH, SCREEN_HEIGHT / 2), (-1, 0))

tick_counter = 0


# This method will be called once per frame
def update():
    global tick_counter

    screen.fill(WHITE)

    # Handle player movement
    player.update(screen)

    if tick_counter % (TRASH_SPAWN_PERIOD * FPS) == 0:
        trash_spawner.spawn()

    trash_spawner.update(screen)

    pygame.display.update()
    clock.tick(FPS)

    tick_counter += 1


# Run until the user asks to quit

running = True

while running:
    # Checking for the user pressing the window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()

# Quit the game
pygame.quit()
