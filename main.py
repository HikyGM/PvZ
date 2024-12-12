import pygame
from pygame import RESIZABLE

from board import Board

WIDTH, HEIGHT = 1000, 600


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
        self.size_window = self.screen.get_size()
        pygame.display.set_caption("PvZ")
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        self.bg = pygame.image.load("data/maps/day.png")
        self.bg = pygame.transform.scale(self.bg, (self.bg.get_width(), self.bg.get_height()))
        self.bg = self.bg.subsurface(pygame.Rect(0, 0, 1000, 600))
        self.bg = pygame.transform.scale(self.bg, self.size_window)

        self.menu_bar_1 = pygame.image.load("data/maps/menu_bar_1.png")

    def main_loop(self):
        board = Board(self.size_window, 9, 5)
        h = 0
        while self.running:

            # if h < 400:
            #     print(h)
            #     self.size_window = self.screen.get_size()
            #     self.bg = pygame.image.load("data/maps/day.png")
            #     self.bg = pygame.transform.scale(self.bg, (self.bg.get_width(), self.bg.get_height()))
            #     self.bg = self.bg.subsurface(pygame.Rect(h, 0, 1000, 600))
            #     self.bg = pygame.transform.scale(self.bg, self.size_window)
            #     h += 5



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame.VIDEORESIZE:
                    self.size_window = self.screen.get_size()
                    self.bg = pygame.image.load("data/maps/day.png")
                    self.bg = pygame.transform.scale(self.bg, (self.bg.get_width(), self.bg.get_height()))
                    self.bg = self.bg.subsurface(pygame.Rect(0, 0, 1000, 600))
                    self.bg = pygame.transform.scale(self.bg, self.size_window)
                    board.resize(*self.size_window)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cell = board.get_click(event.pos)
                    if cell:
                        board.set_plant(cell)
            self.screen.blit(self.bg, (0, 0))
            # self.screen.blit(self.menu_bar_1, (0, 0))
            # resize background image to window size
            board.render(self.screen)
            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.main_loop()
    pygame.quit()
