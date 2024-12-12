import pygame

sunflower = []
for i in range(36):
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))
    sunflower.append(pygame.transform.scale(pygame.image.load(f'data/plants/SunFlower/frame_{i}_delay-0.05s.gif'), (90, 81)))


class Plant(pygame.sprite.Sprite):
    def __init__(self, group, image):
        super().__init__(group)
        self.image = pygame.image.load(f'data/plants/{image}.png').convert_alpha()
        self.rect = self.image.get_rect()


class Sunflower(Plant):
    def __init__(self, group):
        super().__init__(group, 'SunFlower')
        self.life = 100
        self.cost = 50
        self.type = 'Sunflower'

        # Движение
        self.frames_idle_count = 0
        self.frames_idle = sunflower

    def update(self, *args, **kwargs):
        self.frames_idle_count = (self.frames_idle_count + 1) % len(self.frames_idle)
        self.image = self.frames_idle[self.frames_idle_count]
