# Simple pygame program

# Import and initialize the pygame library
import pygame

pygame.init()

size = width, height = 800, 500

# Set up the drawing window
screen = pygame.display.set_mode(size)

# Run until the user asks to quit
running = True
while running:

    # Checking for the user pressing the window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.set_caption("Mini Jam Game")

    # Flip the display
    pygame.display.update()

# Quit the game
pygame.quit()
