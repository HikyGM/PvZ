import pygame

from plant import Plant, Sunflower

FIRST_PLAYER = 1
SECOND_PLAYER = 2

class Board:
    # создание поля
    def __init__(self,size, col, row):
        self.col = col
        self.row = row
        self.board = [[0] * col for _ in range(row)]
        # значения по умолчанию
        self.width, self.height = self.size_window = size
        self.resize(self.width, self.height)

        self.all_sprites = pygame.sprite.Group()
        self.plant_sprites = pygame.sprite.Group()

    def resize(self, width, height):
        self.width, self.height = width, height
        self.left = int(self.width * 0.25)
        self.top = int(self.height * 0.13)
        self.cell_w = int((self.width - self.left - 9) // 9)
        self.cell_h = int((self.height - self.top - self.height * 0.046) // 5)

    def set_plant(self, cell):
        if self.board[cell[0]][cell[1]] == 0:
            plant = Sunflower(self.all_sprites)
            plant.rect.x, plant.rect.y = self.cell_w * cell[1] + self.left, self.cell_h * cell[0] + self.top
            self.board[int(cell[0])][int(cell[1])] = plant

    def render(self, screen):
        transparent_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        # Создаем прозрачную поверхность размером с экран
        transparent_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        for i in range(self.col):
            for e in range(self.row):
                pygame.draw.rect(transparent_surface, pygame.Color(255, 255, 255, 0),  # Альфа-канал 50 (0-255)
                                 pygame.Rect(self.left + i * self.cell_w, self.top + e * self.cell_h, self.cell_w,
                                             self.cell_h), 1)
        # Отображаем прозрачную поверхность на экране
        screen.blit(transparent_surface, (0, 0))
        self.all_sprites.update()
        self.all_sprites.draw(screen)

    def get_cell(self, mouse_pos):
        if self.cell_w * self.col > mouse_pos[0] - self.left > 0 and self.cell_h * self.row > mouse_pos[
            1] - self.top > 0:
            print(self.cell_h)
            return (mouse_pos[1] - self.top) // self.cell_h, (mouse_pos[0] - self.left) // self.cell_w

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        print(cell)
        return cell
