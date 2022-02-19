import pygame
from source.settings import *
from source.game import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_SIZE))

fontsize = 45
smallfont = pygame.font.SysFont("Corbel", fontsize) 

game_title = smallfont.render("Mini Jam 100", True, WHITE)
quit = smallfont.render("Quit" , True , WHITE)
start = smallfont.render("Start" , True , WHITE)

quit_button = pygame.Rect((SCREEN_WIDTH/2 + 20), (SCREEN_HEIGHT/2 + 100), 140, 40)
start_button = pygame.Rect((SCREEN_WIDTH/2 - 160), (SCREEN_HEIGHT/2 + 100), 140, 40)


while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        # Checks for a mouse click
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            # If the mouse is clicked on the quit button the game is terminated 
            if quit_button.x <= mouse[0] <= quit_button.x + quit_button.width and quit_button.y <= mouse[1] <= quit_button.y + quit_button.height: 
                pygame.quit() 

            # When Start button clicked, quits out of while loop and opens game loop
            if SCREEN_WIDTH/2-150 <= mouse[0] <= SCREEN_WIDTH/2 and SCREEN_HEIGHT/2 + 100 <= mouse[1] <= SCREEN_HEIGHT/2 + 140:
                pygame.quit()
                game = Game()
                game.play_game()

 
    screen.fill(MENU_COLOUR) 
      
    
    mouse = pygame.mouse.get_pos() # Sets 'mouse' as a tuple of the mouse coords
      
    # Checks if mouse is over quit button, draws lighter box if i is - Achieves a highlight affect
    if quit_button.x <= mouse[0] <= quit_button.x + quit_button.width and quit_button.y <= mouse[1] <= quit_button.y + quit_button.height: # Quit button Box
        pygame.draw.rect(screen,LIGHT_GREY,[quit_button.x, quit_button.y, quit_button.width, quit_button.height])       
    else: 
        pygame.draw.rect(screen,DARK_GREY,[quit_button.x, quit_button.y, quit_button.width, quit_button.height]) 

    if start_button.x <= mouse[0] <= start_button.x + start_button.width and start_button.y <= mouse[1] <= start_button.y + start_button.height: # Start button Box
        pygame.draw.rect(screen,LIGHT_GREY,[start_button.x, start_button.y, start_button.width, start_button.height])       
    else: 
        pygame.draw.rect(screen,DARK_GREY,[start_button.x, start_button.y, start_button.width, start_button.height]) 
      
    # Blitting text onto screen
    screen.blit(quit, (quit_button.x + quit_button.width/7, quit_button.y))
    screen.blit(start, (start_button.x + start_button.width/7, start_button.y)) 
    screen.blit(game_title, (SCREEN_WIDTH/3, SCREEN_HEIGHT/3)) 
    
    pygame.display.update()