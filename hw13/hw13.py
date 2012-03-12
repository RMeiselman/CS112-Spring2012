#!/usr/bin/env python

## Shoot Um Up Game ##
## Uses "A" and "D" keys to move side to side and "W" to shoot.


import pygame
import os, sys, random, imghdr
from pygame.sprite import Sprite, Group, RenderUpdates
from pygame import *
init()

def load_graphics(filename):
    fullfname = os.path.join('pictures', filename)
    try:
        image = pygame.image.load(fullfname)
    except pygame.error, message:
        print 'Cannot load', fullfname
        raise SystemExit, message
    return image, image.get_rect()


def text_render(text, x, y, color, size):
    font = pygame.font.Font(None, size)
    rend = font.render(text, True, color)
    screen.blit(rend, (x, y))


## Player ##
class Player(Sprite):
    def __init__(self, x = 250, y = 500):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('player.png')
        self.rect.x = x
        self.rect.y = y
        self.add(player_group)

    def update(self, dx, dy):
        if dx > 0 and self.rect.x + dx < 500-self.rect.w:
            self.rect.x += dx
        if dx < 0 and self.rect.x + dx > 0:
            self.rect.x += dx
        if dy > 0 and self.rect.y + dy< 500-self.rect.h:
            self.rect.y += dy 
        if dy < 0 and self.rect.y + dy>0:
            self.rect.y += dy 
        pygame.sprite.groupcollide(player_group, baddies, True, False)

## Player Bullets ##
class Player_Bullets(Sprite):
    def __init__(self, ship, group):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('player_bullets.png')
        self.rect.x = ship.rect.x + 30
        self.rect.y = ship.rect.y
        self.add(group)
    def fire(self):
        if self.rect.y - 16 <= 0:
            self.kill()
        self.rect.y -= 18
        

## Big Enemies ##
class Baddie(Sprite):
    def __init__(self, x, y, status):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('baddie.png')
        self.rect.x = x
        self.rect.y = y
        self.add(baddies)
        self.direction = 1
        self.newy = y + 90
        self.health = 7
        self.status = status

    
    def update(self):
        if self.status == 0:
            self.rect.x += 10
            if self.rect.x >= 60:
                self.status = 1
        elif 50 < self.rect.x + 10*self.direction < 540:
            self.rect.x += 10*self.direction
        elif self.rect.y < self.newy:
            self.rect.y += 25
        else:
            if self.rect.y < 190:
                nbaddie = Baddie(-15,50,0)
            self.direction *= -1
            self.newy += 90

    def hurt(self, amount):
        if self.health - amount <= 0:
            EnemyExplosion((self.rect.x-4,self.rect.y+25))
            self.kill()
        else:
            self.health -= amount

        
## Little Enemies ##
class Little_Baddie(Sprite):
    def __init__(self, x, y, status):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('lilbaddie.png')
        self.rect.x = x
        self.rect.y = y
        self.add(lilbaddies)
        self.direction = 1
        self.newy = y + 90
        self.health = 7
        self.status = status

    def update(self):
        if self.status == 0:
            self.rect.x += 10
            if self.rect.x >= 60:
                self.status = 1
        elif 50 < self.rect.x + 20*self.direction < 540:
            self.rect.x += 20*self.direction
        elif self.rect.y < self.newy:
            self.rect.y += 25
        else:
            if self.rect.y < 190:
                nlilbaddie = Little_Baddie(-15,50,0)
            self.direction *= -1
            self.newy += 90

    def hurt(self, amount):
        if self.health - amount <= 0:
            EnemyExplosion((self.rect.x - 4, self.rect.y + 25))
            self.kill()
        else:
            self.health -= amount

## Explosions ##
class EnemyExplosion(Sprite):
    def __init__(self, position):
        Sprite.__init__(self)
        self.position = position
        self.duration = 10
        self.expandto = 18
        self.radius = 5
        self.add(explosions)
        
    def update(self):
        if self.expandto > self.radius:
            self.radius += 3
        else:
            self.kill()

    def random_color(self):
        return ((random.randrange(120, 256), 255, random.randrange(120, 256)))

    def draw(self, surf):
        pygame.draw.circle(surf, self.random_color(), self.position, self.radius)


## Constants ##
BLACK = 0, 0, 0
WHITE = 255, 255, 255

SCREEN_SIZE = 500, 700
FPS = 30


## Initialize ##
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
game = False
begin = True
screen.fill(BLACK)
pygame.display.set_caption('Bunny Hop: Attack of the Baddies')
bun_icon = image.load('bun_icon.png')
pygame.display.set_icon(bun_icon)

screen_rect = pygame.Rect((0, 0), (600, 600))
info_rect = pygame.Rect((600, 0), (200, 600))

bounds = screen_rect

pygame.draw.rect(screen, (210, 210, 210), info_rect)
pygame.draw.line(screen, WHITE, (600, 0), (600, 600), 3)

player_group = Group()
player = Player()

player_bullets = Group()

baddies = Group()
lilbaddies = Group()

explosions = Group()

score = len(explosions)

done = False

## Starting Positions for Both Baddies ##
bx = 50
by = 50
for i in range(10):
    p = Baddie(bx, by, 1)
    bx += 100

bx2 = 200
by2 = 200
for i in range(20):
    p = Little_Baddie(bx2, by2, 1)
    bx2 += 60


pygame.key.set_repeat(45, 1)

move = 0

## Start Screen ##
pygame.draw.rect(screen,BLACK,screen_rect)
text_render("Help Bunny kill the Baddies by shooting them with carrots!!", 20, 190, WHITE, 22)
text_render("Use 'A' and 'D' to move and use 'W' to fire carrots.", 20, 225, WHITE, 28)
text_render("Press space to begin.", 65, 258, WHITE, 50)

while begin:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            begin = False
        elif evt.type == KEYDOWN: 
            if evt.key == K_ESCAPE:
                begin = False
            if evt.key == K_SPACE:
                game = True
                begin = False


    pygame.display.flip()
    clock.tick(FPS)

## Game Loop ##
while done == False:
    pygame.draw.rect(screen,BLACK,screen_rect)

    
## Keyboard Commands ##
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN: 
            if evt.key == K_ESCAPE:
                done = True
            if evt.key == K_w:
                missle = Player_Bullets(player, player_bullets)

## Player Movement Controls ##
    pressed = pygame.key.get_pressed()
    if pressed[K_a]:
        player.update(-6, 0)
    if pressed[K_d]:
        player.update(6, 0)

 ## Update Both Baddies ##
    if move < 2:
        move += 1
    else:
        baddies.update()
        move = 0

    if move < 2:
        move += 1
    else:
        lilbaddies.update()
        move = 0
    
## Update Bullets ##
    for i in player_bullets:
        i.fire()
        player_bullets.draw(screen)

    for enemy in pygame.sprite.groupcollide(baddies, player_bullets, False, True):
        enemy.hurt(1)
    
    for enemy in pygame.sprite.groupcollide(lilbaddies, player_bullets, False, True):
        enemy.hurt(1)

## Score ##
        score = len(explosions)
        text_render("Score:",400,600,WHITE,30)

## Update explosions ##     
    for i in explosions:
        i.update()
        i.draw(screen)

## Player Death ##
    if pygame.sprite.groupcollide(player_group, baddies, True, True) or  pygame.sprite.groupcollide(player_group, lilbaddies, True, True) == True:
        done == True
        break
   
    
## Draw ##   
    player_group.draw(screen)
    baddies.draw(screen)
    lilbaddies.draw(screen)


## Update ##
    pygame.display.flip()
    clock.tick(FPS)
