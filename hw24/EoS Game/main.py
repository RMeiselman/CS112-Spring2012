#!/usr/bin/env python

import sys
import pygame
from pygame import *
from random import randrange
from pygame.locals import K_ESCAPE
from pygame.sprite import spritecollide, Sprite, Group, RenderUpdates
class ApplicationState(object):
    def __init__(self, app):
        self.app = app
        self.setup()

    def setup(self): pass
    def resume(self): pass
    def handle_event(self, event): pass
    def update(self): pass
    def draw(self, screen): pass
class MainMenu(ApplicationState):
    fg_color = 255,255,255
    bg_color = 0,0,0
    flash_rate = 500

    def setup(self):
        font = pygame.font.Font(None, 60)

        font.set_bold(True)
        self.title = font.render("Super Coin Get", True, self.fg_color, self.bg_color)

        font.set_bold(False)
        font.set_italic(True)
        self.inst = font.render("Press <SPACE> to Start", True, self.fg_color, self.bg_color)

    def resume(self):
        self.clock = pygame.time.Clock()
        self.time = 0

    def handle_event(self, event):
        if event.type == KEYDOWN and (event.key == K_q or event.key == K_ESCAPE):
            self.app.quit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            self.app.set_state(Game)

    def update(self):
        self.time += self.clock.tick()
        self.time %= 2 * self.flash_rate
        self.draw_inst = self.time < self.flash_rate


    def draw(self, screen):
        bounds = screen.get_rect()

        screen.fill(self.bg_color)
        
        rect = self.title.get_rect()
        rect.center = bounds.centerx, bounds.centery - bounds.height / 4
        screen.blit(self.title, rect)

        if self.draw_inst:
            rect = self.inst.get_rect()
            rect.center = bounds.centerx, bounds.centery + bounds.height / 4
            screen.blit(self.inst, rect)

class Level(object):
    initial_cookies = 20

    def __init__(self, size):
        self.bounds = Rect((0,0), size)

    def restart(self):
        self.player = Player()
        self.player.rect.center = self.bounds.center

        self.cookies = CoinGroup(self.bounds)

        # create initial coins
        for i in range(self.initial_coins):
            self.cookies.spawn()
    
    def update(self, dt):
        self.player.update(dt)
        self.cookies.update(dt)

        # lock player in bounds
        self.player.rect.clamp_ip(self.bounds)

        # collide player with coins
        spritecollide(self.player, self.cookies, True)


def text_render(text, x, y, color, size):
    font = pygame.font.Font(None, size)
    rend = font.render(text, True, color)
    screen.blit(rend, (x,y))
    
class Sprite:
    def __init__ (self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = image.load(filename)
        self.bitmap.set_colorkey((-1))
    def set_position(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))
        
def Intersect(s1_x, s1_y, s2_x, s2_y):
    if (s1_x > s2_x - 75) and (s1_x < s2_x + 75) and (s1_y > s2_y - 75) and (s1_y < s2_y + 75):
        return 1
    else:
        return 0
####COOKIES FOR POINTS####
COOKIE_SPAWN_RATE = 3
COOKIE_N_STARTING = 30
class Cookie(Sprite):
    def __init__(self, loc):
        Sprite.__init__(self)

        self.image = image.load("cookie_door_left")
        self.rect = self.image.get_rect()
        self.rect.center = loc

    def update(self, dt):
        self.anim.update(dt)
        self.image = self.anim.get_current_frame()

class CookieGroup(Group):
    spawn_rate = 1000
    def __init__(self, bounds):
        Group.__init__(self)

        self.bounds = bounds
        self.spawn_timer = 0

    def spawn(self):
        x = randrange(self.bounds.x, self.bounds.x + self.bounds.width)
        y = randrange(self.bounds.y, self.bounds.y + self.bounds.height)

        cookie = Cookie((x,y))
        cookie.rect.clamp_ip(self.bounds)
        self.add(cookie)

    def update(self, dt):
        Group.update(self, dt)

        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_rate:
            self.spawn()
            self.spawn_timer = 0
            
icon = image.load("pye_straight_on.bmp")
init()
screen = display.set_mode((900, 700))
key.set_repeat(1,1)
display.set_caption('The Elements of Sundae :)')
backdrop = image.load("EoS_Background.bmp")
FPS = 30
pygame.display.set_icon(icon)

enemies = []

x = 0

for count in range(5):
    enemies.append(Sprite(125 * x + 50, 50, 'enemy_straight_on.bmp'))
    x += 1

hero = Sprite(500, 680, 'pye_straight_on.bmp')
ourmissileup = Sprite(0,200, 'bullet_up.bmp')
ourmissiledown = Sprite(0,200, 'bullet_down.bmp')
ourmissileleft = Sprite(0,200, 'bullet_left.bmp')
ourmissileright = Sprite(0,200, 'bullet_right.bmp')
bomb = Sprite(0,50, 'bombs_small.bmp')


enemyspeed = 2

class Game(object):
    def __init__(self, screen):
        self.level = Level(self.screen.get_size())
        self.cookies = CookieGroup(self.level.bounds)

        for i in range(COOKIE_N_STARTING):
            self.cookies.spawn()

    def update(self):
        self.cookies.update
        for cookie in spritecollide(self.hero, self.cookies, True):
            self.score += 1

        self.cam.update(self.player.rect)

    def draw(self):
        for coin in self.coins:
            self.cam.draw_sprite(self.game_area, cookie)
initial_cookies = 20
screen_rect = pygame.Rect((0, 0), (900,700))
info_rect = pygame.Rect((600, 0), (200, 700))
BLACK = 0, 0, 0
WHITE = 255, 255, 255
pygame.draw.rect(screen, (210, 210, 210), info_rect)
pygame.draw.line(screen, WHITE, (600, 0), (600, 600), 3)
done = False
begin = True
game = False
screen.fill(BLACK)
###Start Screen###
pygame.draw.rect(screen,BLACK,screen_rect)
text_render("Help Sweetie kill the Ice Cream Bats and collect the coins for points!!", 20, 190, WHITE, 22)
text_render("Use 'WASD' to move, and use the arrow keys to shoot!", 20,225, WHITE, 28)
text_render("Press space to begin.", 65, 258, WHITE, 50)
while begin:
    for ourevent in event.get():
        if ourevent.type == QUIT:
            begin = False
        elif ourevent.type == KEYDOWN:
            if ourevent.key == K_ESCAPE:
                begin = False
            if ourevent.key == K_SPACE:
                game = True
                begin = False
while done == False:
    screen.blit(backdrop, (0, 0))
    
    for count in range(len(enemies)):
        enemies[count].y += + enemyspeed
        enemies[count].render()

    if enemies[len(enemies)-1].y > 699:
        enemyspeed = -2
        for count in range(len(enemies)):
            enemies[count].x += 5

    if enemies[0].y < 10:
        enemyspeed = 2
        for count in range(len(enemies)):
            enemies[count].x += 5

    if ourmissileleft.x < 699 and ourmissileleft.x > 0:
        ourmissileleft.render()
        ourmissileleft.x -= 5

    if ourmissiledown.y < 699 and ourmissiledown.y > 0:
        ourmissiledown.render()
        ourmissiledown.y += 5

    if ourmissileup.y < 699 and ourmissileup.y > 0:
        ourmissileup.render()
        ourmissileup.y -= 5

    if ourmissileright.x < 699 and ourmissileright.x > 0:
        ourmissileright.render()
        ourmissileright.x += 5

    if bomb.x < 699 and bomb.x > 0:
        bomb.render()

    for count in range(0, len(enemies)):
        if Intersect(ourmissileup.x, ourmissileup.y, enemies[count].x, enemies[count].y):
            del enemies[count]
            break
        elif Intersect(ourmissiledown.x, ourmissiledown.y, enemies[count].x, enemies[count].y):
            del enemies[count]
            break
        elif Intersect(ourmissileleft.x, ourmissileleft.y, enemies[count].x, enemies[count].y):
            del enemies[count]
            break
        elif Intersect(ourmissileright.x, ourmissileright.y, enemies[count].x, enemies[count].y):
            del enemies[count]
            break
        elif Intersect(bomb.x, bomb.y, enemies[count].x, enemies[count].y):
            del enemies[count]
            break

    if len(enemies) == 0:
        pygame.quit()
        sys.exit()

    for ourevent in event.get():
        if ourevent.type == KEYDOWN:
            if ourevent.key == K_ESCAPE:
                quit = 1
            if ourevent.key == K_d and hero.x < 890:
                hero.x += 5
            if ourevent.key == K_a and hero.x > 10:
                hero.x -= 5
            if ourevent.key == K_s and hero.y < 690:
                hero.y += 5
            if ourevent.key == K_w and hero.y > 10:
                hero.y -= 5
            if ourevent.key == K_UP:
                ourmissileup.x = hero.x
                ourmissileup.y = hero.y
            if ourevent.key == K_DOWN:
                ourmissiledown.x = hero.x
                ourmissiledown.y = hero.y
            if ourevent.key == K_LEFT:
                ourmissileleft.x = hero.x
                ourmissileleft.y = hero.y
            if ourevent.key == K_RIGHT:
                ourmissileright.x = hero.x
                ourmissileright.y = hero.y
            if ourevent.key == K_g:
                bomb.x = hero.x
                bomb.y = hero.y



    hero.render()
    display.update()
    time.delay(2)
