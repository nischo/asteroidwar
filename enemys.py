import pygame
import random

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('asteroid.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(600-32)
        self.rect.y = 10
        self.speedx = random.randrange(1,4)
        self.speedy = random.randrange(1,4)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > 600 or self.rect.left <= 0:
            self.speedx *= -1
            
        if self.rect.bottom >= 800:
            self.kill()
