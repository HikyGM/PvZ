import pygame

class Plant(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('data/plants/SunFlower.png').convert_alpha()
        self.rect = self.image.get_rect()
