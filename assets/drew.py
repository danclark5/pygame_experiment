import pygame
from util import load_image

class Drew(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("drew.png", -1)
        self.next_position = position
        self.position = position

    def update(self):
        self.rect.center= self.position
        pass

    def walk(self, walk_values, obstacles):
        for key, distance in walk_values.items():
            self.next_position = self.position.copy()
            self.calculate_next_position(key, distance)
            if not self.is_blocked(obstacles):
                self.position = self.next_position

    def is_blocked(self, obstacles):
        print(self.is_blocked_by_screen_edge())
        if self.is_blocked_by_screen_edge():
            return True
        if self.is_blocked_by_obstacles(obstacles):
            return True
        return False

    def is_blocked_by_screen_edge(self):
        screen_size = pygame.display.get_window_size()
        if self.next_position[0] < 0 or self.next_position[0] > screen_size[0] \
                or self.next_position[1] < 0 or self.next_position[1] > screen_size[1]:
            return True
        return False

    def is_blocked_by_obstacles(self, obstacles):
        return False
        # Cycle through obstacles
            # Check if obstacle and drew hit
            # ToDo: If this obstacle is an enemy or projectile then inflict
            # damage. Although it would be neat to be deflect projectiles.

    def calculate_next_position(self, key, distance):
        walk_call = {
            pygame.K_w: self.walk_north, \
            pygame.K_d: self.walk_east, \
            pygame.K_s: self.walk_south, \
            pygame.K_a: self.walk_west}

        walk_call[key](distance)

    def walk_north(self, distance):
        self.next_position[1] -= distance

    def walk_south(self, distance):
        self.next_position[1] += distance

    def walk_east(self, distance):
        self.next_position[0] += distance

    def walk_west(self, distance):
        self.next_position[0] -= distance

