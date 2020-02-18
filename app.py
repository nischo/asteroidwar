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


class Game(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.size = 600, 800
        self.screen = pygame.display.set_mode(self.size)
        self.black = 255, 87, 33

    def update(self):
        self.screen.fill(BLACK)

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

    # bullets.update()
    all_sprites.update()

    # check if a bullet hits the asteroid
    hits = pygame.sprite.groupcollide(enemys, bullets, True, True)

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
