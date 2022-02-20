import pygame

from enum import Enum
from source.settings import *
from source.game import *

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Mini Jam 100")

fontsize = 45
small_font = pygame.font.SysFont("Corbel", fontsize)


class MenuType(Enum):
    START = 0,
    GAME_OVER = 1


class Menu:
    def __init__(self, menu_type: MenuType, score=0):
        self.score = score
        self.menu_type = menu_type

        self.mouse = pygame.mouse.get_pos()  # Sets 'mouse' as a tuple of the mouse coords

        self.draw_start()

    def draw_start(self):
        main_text = "Mini Jam 100" if self.menu_type == MenuType.START else "Game Over!"
        button_one_text = "Play" if self.menu_type == MenuType.START else "Play again"

        game_title = small_font.render(main_text, True, WHITE)
        quit_text = small_font.render("Quit", True, WHITE)
        start_text = small_font.render(button_one_text, True, WHITE)

        quit_button = pygame.Rect(((SCREEN_WIDTH / 2) + 20), (SCREEN_HEIGHT / 2 + 100), 140, 40)
        start_button = pygame.Rect(((SCREEN_WIDTH / 2) - 160), (SCREEN_HEIGHT / 2 + 100), 140, 40)

        while True:
            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    pygame.quit()

                    # Checks for a mouse click
                if ev.type == pygame.MOUSEBUTTONDOWN:

                    # If the mouse is clicked on the quit button the game is terminated
                    if quit_button.x <= self.mouse[0] <= quit_button.x + quit_button.width and quit_button.y <= self.mouse[1] \
                            <= quit_button.y + quit_button.height:
                        pygame.quit()

                        # When Start button clicked, quits out of while loop and opens game loop
                    if SCREEN_WIDTH / 2 - 150 <= self.mouse[0] <= SCREEN_WIDTH / 2 and SCREEN_HEIGHT / 2 + 100 <= self.mouse[1] \
                            <= SCREEN_HEIGHT / 2 + 140:
                        pygame.quit()
                        game = Game()
                        game.play_game()

            screen.fill(MENU_COLOUR)

            self.mouse = pygame.mouse.get_pos()  # Update the mouse position

            # Checks if mouse is over menu buttons, draws lighter box if 'i' is - Achieves a highlight affect
            self.check_mouse_hover(quit_button)
            self.check_mouse_hover(start_button)

            # Blitting text onto screen
            screen.blit(quit_text, (quit_button.x + 25, quit_button.y))
            screen.blit(start_text, (start_button.x + 25, start_button.y))
            screen.blit(game_title, ((SCREEN_WIDTH / 2) - (game_title.get_width() / 2), SCREEN_HEIGHT / 3))

            pygame.display.update()

    def check_mouse_hover(self, button):
        if button.x <= self.mouse[0] <= button.x + button.width and button.y <= self.mouse[
            1] <= button.y + button.height:  # Quit button Box
            pygame.draw.rect(screen, LIGHT_GREY, [button.x, button.y, button.width, button.height])
        else:
            pygame.draw.rect(screen, DARK_GREY, [button.x, button.y, button.width, button.height])


if __name__ == "__main__":
    menu = Menu(MenuType.START)
