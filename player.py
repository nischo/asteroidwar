import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('spaceship.png').convert()
        self.rect = self.image.get_rect()
        self.rect.y = 730
        self.rect.x = 268
        self.speedx = 0
    
    def update(self):
        self.speedx = 0

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10

        self.rect.x += self.speedx


        if self.rect.right > 600 or self.rect.left  <= 0:
            self.speedx = 0
    
    def shoot(self, bullets):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets.add(bullet)
        pass
        