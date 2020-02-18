import pygame
import random
import os
import sys
from player import Player
from bullet import Bullet
from enemys import Enemy

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
HIGHT = 800
WIDTH = 600
score = 1

class Game(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.size = WIDTH, HIGHT
        self.screen = pygame.display.set_mode(self.size)
        self.black = 255, 87, 33
        self.font = pygame.font.SysFont("arial", 32)
        self.text = self.font.render("Score: ", True, (WHITE))
        self.score = self.font.render( str(score), True, (WHITE))
    
    def update(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.text, (0,0))
        self.score = self.font.render( str(score), True, (WHITE))
        self.screen.blit(self.score, (100,0))

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Asteroid War!!")



game = Game()
player = Player()

all_sprites = pygame.sprite.Group()
player_list = pygame.sprite.Group()
enemys = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player_list.add(player)
all_sprites.add(player)

for i in range(10):
    enemy = Enemy()
    enemys.add(enemy)
    all_sprites.add(enemy)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.speed = 4
            if event.key == pygame.K_LEFT:
                player.speed = -4
            if event.key == pygame.K_SPACE:
                player.shoot(bullets)
                all_sprites.add(bullets)

    all_sprites.update()

    # check if a bullet hits the asteroid
    hits = pygame.sprite.groupcollide(enemys, bullets, True, True)

    if hits:
        score += 1
        print(score)

    for hit in hits:
        enemy = Enemy()
        enemys.add(enemy)
        all_sprites.add(enemy)
        
    # check if a asteroid hits the ship
    hits = pygame.sprite.spritecollide(player, enemys, False)

    if hits:
        print("Game Over")
        running = False
        sys.exit()

    game.update()

    all_sprites.draw(game.screen)

    pygame.display.update()

    clock.tick(FPS)
