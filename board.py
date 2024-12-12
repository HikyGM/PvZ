import pygame

import plant
from plant import Plant, Sunflower

FIRST_PLAYER = 1
SECOND_PLAYER = 2


class Board:
    # создание поля
    def __init__(self, size, col, row):
        self.col = col
        self.row = row
        self.board = [[0] * col for _ in range(row)]
        # значения по умолчанию
        self.width, self.height = self.size_window = size

        self.all_sprites = pygame.sprite.Group()
        self.plant_sprites = pygame.sprite.Group()
        self.resize(self.width, self.height)

    def resize(self, width, height):
        width_ratio = width / self.width
        height_ratio = height / self.height

        for row in range(self.row):
            for col in range(self.col):
                if isinstance(self.board[row][col], Sunflower):
                    plant = self.board[row][col]
                    # Вычисляем новую позицию относительно левого края
                    new_x = (plant.rect.x - self.left) * width_ratio + (width * 0.25)
                    # Вычисляем новую позицию относительно верхнего края
                    new_y = (plant.rect.y - self.top) * height_ratio + (height * 0.13)
                    plant.rect.x = int(new_x)
                    plant.rect.y = int(new_y)

        self.width, self.height = width, height
        self.left = int(self.width * 0.25)
        self.top = int(self.height * 0.13)
        self.cell_w = int((self.width - self.left - 9) // 9)
        self.cell_h = int((self.height - self.top - self.height * 0.046) // 5)

        # Обновляем размеры всех растений
        for sprite in self.all_sprites:
            if isinstance(sprite, Sunflower):
                sprite.resize(self.cell_w, self.cell_h)



    def set_plant(self, cell):
        if self.board[cell[0]][cell[1]] == 0:
            plant = Sunflower(self.all_sprites, self.cell_w, self.cell_h)
            plant.rect.x, plant.rect.y = self.cell_w * cell[1] + self.left, self.cell_h * cell[0] + self.top
            self.board[int(cell[0])][int(cell[1])] = plant

    def render(self, screen):
        transparent_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        for i in range(self.col):
            for e in range(self.row):
                pygame.draw.rect(transparent_surface, pygame.Color(255, 255, 255, 0),
                                 pygame.Rect(self.left + i * self.cell_w, self.top + e * self.cell_h, self.cell_w,
                                             self.cell_h), 1)

        screen.blit(transparent_surface, (0, 0))
        self.all_sprites.update(self.cell_w, self.cell_h)
        self.all_sprites.draw(screen)

    def get_cell(self, mouse_pos):
        if self.cell_w * self.col > mouse_pos[0] - self.left > 0 and self.cell_h * self.row > mouse_pos[
            1] - self.top > 0:
            return (mouse_pos[1] - self.top) // self.cell_h, (mouse_pos[0] - self.left) // self.cell_w

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        return cell
