import pygame
import random
import os
import sys
from player import Player
from bullet import Bullet
from enemys import Enemy

# declare some constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN =(0,255,0)
FPS = 60
HIGHT = 800
WIDTH = 600
ASTEROIDS = 5
LIVE = 3

health = 100
score = 0

class Game(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.size = WIDTH, HIGHT
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.SysFont("arial", 32)
        self.text = self.font.render("Score: ", True, (WHITE))
        self.score = self.font.render( str(score), True, (WHITE))
        self.live = pygame.image.load('spaceship.png').convert()
        self.live = pygame.transform.scale(self.live, (30,30))
        
    
    def update(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.text, ((WIDTH-180)/2,0))
        self.score = self.font.render( str(score), True, (WHITE))
        self.screen.blit(self.score, (WIDTH/2,0))
        
        self.healthBorder = pygame.Rect(20,10,100,20)
        self.health = pygame.Rect(20,10,health,20)
        pygame.draw.rect(self.screen, GREEN, self.health)
        pygame.draw.rect(self.screen, WHITE, self.healthBorder,2)

        for i in range(LIVE):
            self.screen.blit(self.live, [WIDTH - (i*40) - 40,10])
        
        

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Asteroid War!!")


#create Game and Player objects
game = Game()
player = Player()

#initialized  sprite Group
all_sprites = pygame.sprite.Group()
player_list = pygame.sprite.Group()
enemys = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# add player to sprite Groupe
player_list.add(player)
all_sprites.add(player)

#create Asteroids at start
for i in range(ASTEROIDS):
    enemy = Enemy()
    enemys.add(enemy)
    all_sprites.add(enemy)

running = True

# game loop
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


    #for e in enemys:
      #print('enemy:' + str(e.rect.bottom))
     # if e.rect.bottom >= 792:
        #print(e.rect)
        #e.kill()
        #enemy = Enemy()
        #enemys.add(enemy)
        #all_sprites.add(enemy)
        
    # check if a asteroid hits the ship
    hits = pygame.sprite.spritecollide(player, enemys, True, pygame.sprite.collide_circle)

    for e in enemys:
        if e.rect.bottom >= 800:
            print(e.rect)
            e.kill()
            enemy = Enemy()
            enemys.add(enemy)
            all_sprites.add(enemy)
   
    if hits:
        enemy = Enemy()
        enemys.add(enemy)
        all_sprites.add(enemy)

        
    if hits and LIVE >= 1:
        health -= 25

        if health <= 0:
            health = 100
            LIVE -= 1
    
    if LIVE < 1:
 
        print("Game Over")
        running = False
        sys.exit()

    game.update()
    all_sprites.draw(game.screen)
    pygame.display.update()

    clock.tick(FPS)

