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
        for key, distance in walk_values.items():
            self.call_walk(key, distance)

    def call_walk(self, key, distance):
        walk_call = {
            pygame.K_w: self.walk_north, \
            pygame.K_d: self.walk_east, \
            pygame.K_s: self.walk_south, \
            pygame.K_a: self.walk_west}

        walk_call[key](distance)

    def walk_north(self, distance):
        self.position[1] -= distance

    def walk_south(self, distance):
        self.position[1] += distance

    def walk_east(self, distance):
        self.position[0] += distance

    def walk_west(self, distance):
        self.position[0] -= distance

