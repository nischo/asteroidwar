import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.image.load('bomb.png'), -90)
        self.rect = self.image.get_rect()
        
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -8
    
    def update(self):
        self.rect.y += self.speed

        if self.rect.top < 0:
            self.kill()