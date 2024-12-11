import pygame

from board import Board

WIDTH, HEIGHT = 1000, 600


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("PvZ")
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        self.bg = pygame.image.load("data/maps/day.png")
        self.menu_bar_1 = pygame.image.load("data/maps/menu_bar_1.png")

    def main_loop(self):
        board = Board(9, 5)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cell = board.get_click(event.pos)
                    if cell:
                        board.set_plant(cell)
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.menu_bar_1, (0, 0))
            board.render(self.screen)
            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.main_loop()
    pygame.quit()
