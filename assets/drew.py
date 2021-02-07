import pygame
from util import load_image

class Drew(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("drew.png", -1)
        self.position = position

    def update(self):
        self.rect.midtop = self.position
        pass

    def walk(self, walk_values):
        self.position[0] += walk_values[0]
        self.position[1] += walk_values[1]

