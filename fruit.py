import random

import pygame
from pygame import sprite, Rect

from data.exceptions import BadLoadImage
from data.commands import load_image
from settings import WIDTH, HEIGHT, Y_GRAVITY, FPS, SIZE

fruit_types = ['a', 'b', 'c', 'l', 'r', 'w']


class Fruit(sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.x = random.randint(20, WIDTH - 20)
        self.y = random.randint(HEIGHT, HEIGHT + 100)

        self.fruit = random.choice(fruit_types)

        self.image = self.load_fruit_image()
        self.rect = Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

        self.throwing_force = -800
        self.x_velocity = random.randrange(*(-3, 0) if self.x >= WIDTH / 2 else (0, 3))

    def update(self):
        x = self.rect.x
        y = self.rect.y

        self.throwing_force += Y_GRAVITY
        y += self.throwing_force / FPS

        x += self.x_velocity

        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect.size)

    def load_fruit_image(self):
        path = 'res/sprites/fruits'
        try:
            return load_image(f'{path}/{self.fruit}/{self.fruit}0.png')
        except BadLoadImage as bli:
            print(bli)