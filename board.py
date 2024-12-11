import pygame

from plant import Plant

FIRST_PLAYER = 1
SECOND_PLAYER = 2


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 250
        self.top = 85
        self.cell_w = 81
        self.cell_h = 97

        self.all_sprites = pygame.sprite.Group()
        self.plant_sprites = pygame.sprite.Group()

    def set_plant(self, cell):
        if self.board[cell[0]][cell[1]] == 0:
            p = Plant(self.all_sprites)
            p.rect.x, p.rect.y = self.cell_w * cell[1] + self.left, self.cell_h * cell[0] + self.top
            self.board[cell[0]][cell[1]] = 1

    def render(self, screen):
        for i in range(self.width):
            for e in range(self.height):
                pygame.draw.rect(screen, pygame.Color("white"),
                                 pygame.Rect(self.left + i * self.cell_w, self.top + e * self.cell_h, self.cell_w,
                                             self.cell_h), 1)
        self.all_sprites.draw(screen)

    def get_cell(self, mouse_pos):
        if self.cell_w * self.width > mouse_pos[0] - self.left > 0:
            if mouse_pos[1] - self.top < self.cell_h * self.height:
                return (mouse_pos[1] - self.top) // self.cell_h, (mouse_pos[0] - self.left) // self.cell_w

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        return cell
