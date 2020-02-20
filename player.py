import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('spaceship.png').convert()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.75/ 2)
        #pygame.draw.circle(self.image, (255,34,55), self.rect.center, self.radius)
        self.rect.y = 730
        self.rect.x = 268
        self.speedx = 0
        
    def update(self):
        
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 10
        else:
            self.speedx = 0

        self.rect.x += self.speedx

        if self.rect.right >= 600: 
            self.rect.x = (600 - 64)

        if self.rect.left  <= 0:
            self.rect.x = 0
    
    def shoot(self, bullets):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets.add(bullet)
        pass
        