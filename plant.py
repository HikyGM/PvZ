import pygame

sunflower = []
for i in range(36):
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))


class Plant(pygame.sprite.Sprite):
    def __init__(self, group, image, width, height):
        super().__init__(group)
        self.image = pygame.image.load(f'data/plants/{image}.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = width, height

    def update_size(self, width, height):
        self.width, self.height = width, height

class Sunflower(Plant):
    def __init__(self, group, width, height):
        super().__init__(group, 'SunFlower', width, height)
        self.life = 100
        self.cost = 50
        self.type = 'Sunflower'
        # Движение
        self.frames_idle_count = 0
        self.frames_idle = sunflower
        self.animation_speed = 10  # Новый атрибут: каждый 5-й кадр будет обновляться анимация
        self.animation_counter = 0  # Счетчик для отслеживания кадров

    def update(self, *args, **kwargs):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.frames_idle_count = (self.frames_idle_count + 1) % len(self.frames_idle)
        
        self.image = pygame.transform.scale(self.frames_idle[self.frames_idle_count], (args[0], args[1]))
    def resize(self, width, height):
        # Обновление размера спрайта
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=self.rect.center)