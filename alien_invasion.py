import sys
import pygame


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
