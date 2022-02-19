# Import and initialize the pygame library

import pygame
from player import *
from settings import *
from Incinerator import *

#pygame.init()
#
## Set up the drawing window
#
#screen = pygame.display.set_mode(SCREEN_SIZE)
#pygame.display.set_caption("Mini Jam Game")
#background_image = pygame.image.load('Mini Jam 100/minijam-100/resources/test-background.png')
#background = pygame.transform.scale(background_image, SCREEN_SIZE)
#
#clock = pygame.time.Clock()
#
## Run until the user asks to quit
#
#running = True
#while running:
#
#    clock.tick(FPS)
#
#    # Checking for the user pressing the window close button
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#
#    #screen.fill(WHITE)
#    screen.blit(background,(0,0))
#    # Handle player movement
#
#    player.player_movement()
#    player.update(screen)
#
#    # Flip the display
#
#    pygame.display.update()
#
## Quit the game
#pygame.quit()

class Game:

    def __init__(self):
        pygame.init()
        self.window_setup()
        self.clock = pygame.time.Clock()
        self.player = Player((SCREEN_WIDTH/2 - 32, SCREEN_HEIGHT/2 - 32))
        self.incin = Incinerator((0, 0))
        

    def window_setup(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE) 
        pygame.display.set_caption("Mini Jam Game")
        self.screen.fill(WHITE)

    def update(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.incin.incin_surface, self.incin.pos)
        self.player.update(self.screen) # Updates player behaviour

    def play_game(self):
        running = True

        while running:
            self.clock.tick(FPS) # Sets game FPS
            
            for event in pygame.event.get(): # Checking for the user pressing the window close button
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN: # Checking for Space key (size_up)
                    if event.key == pygame.K_p:
                        self.player.upgrade(size_up = True)
                if event.type == pygame.KEYDOWN: # Checking for Space key (size_up)
                    if event.key == pygame.K_o:
                        self.player.upgrade(speed_up = True)

            self.update()
            pygame.display.update()
        
        pygame.quit() # Quit the game once running == False

game = Game()
game.play_game()

