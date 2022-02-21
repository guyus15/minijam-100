from source.player import *
from source.settings import *
from source.trash_spawner import TrashSpawner
from source.incinerator import Incinerator
from source.vector import Vector
from source.level import Level
from source.time_manager import TimeManager
from main import Menu
from main import MenuType


class Game:

    def __init__(self):
        pygame.init()
        self.screen = None
        self.window_setup()
        self.clock = pygame.time.Clock()
        self.player = Player((SCREEN_WIDTH / 2 - 32, SCREEN_HEIGHT / 2 - 32))
        self.incinerator = Incinerator(Vector(20, 0), Vector(100, 100), self.player)
        self.trash_spawners = [TrashSpawner(Vector(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100), (0, -1), self.player),
                               TrashSpawner(Vector(SCREEN_WIDTH / 2, 100), (0, 1), self.player)]
        self.level = Level()
        self.background_image = pygame.Surface.convert(pygame.image.load(BACKGROUND_IMAGE_PATH))
        self.total_trash = 0
        self.small_font = pygame.font.SysFont("Corbel", FONT_SIZE)

    def window_setup(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Mini Jam Game")

    def update(self):
        # Load the background image
        self.screen.blit(self.background_image, (0, 0))

        self.incinerator.update(self.screen)  # Updates incinerator behaviour
        for trash_spawner in self.trash_spawners:
            trash_spawner.update(self.screen)  # Updates trash spawner behaviour
            self.total_trash = trash_spawner.get_number_trash()
        self.player.update(self.screen)  # Updates player behaviour

        self.check_game_over()

        colour = WHITE if self.total_trash < TRASH_UNTIL_GAME_OVER - 5 else RED

        items_text = self.small_font.render(str(self.total_trash) + "/" + str(TRASH_UNTIL_GAME_OVER), True, colour)
        self.screen.blit(items_text, (TRASH_TEXT_X, TRASH_TEXT_Y))

        TimeManager.tick()

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

    def check_game_over(self):
        if self.total_trash >= TRASH_UNTIL_GAME_OVER:
            pygame.quit()
            Menu(MenuType.GAME_OVER)
