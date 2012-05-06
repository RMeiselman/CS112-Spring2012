#!/usr/bin/env python
"""
game.py

"""

import pygame
from pygame.locals import *
from pygame.sprite import spritecollide, GroupSingle
from app import ApplicationState
from level import Level

class MainMenu(ApplicationState):
    fg_color = 255,255,255
    bg_color = 0,0,0
    flash_rate = 500

    def setup(self):
        font = pygame.font.font(None, 80)
        font.set_bold(True)
        self.title = font.render("Super Coin Get", True, self.fg_color, self.bg_color)
        font.set_bold(False)
        self.set_italic(True)
        self.inst = font.render("Press <SPACE> to Start", True, self.fg_color, self.bg_color)

    def resume(self):
        self.clock = pygame.time.Clock()
        self.time = 0

    def handle_event(self, event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
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
            rect.center = bounds.centerx, bounds.centery - bounds.height / 4
            screen.blit(self.inst, rect)
            
class Game(ApplicationState):
    fps = 60

    def setup(self):
        self.level = Level(self.app.screen.get_size())
        self.level.restart()

    def resume(self):
        self.clock = pygame.time.Clock()
        pygame.mixer.music.unpause()

    def update(self):
        dt = self.clock.tick(self.fps)
        self.level.update(dt)

    def draw(self, screen):
        self.level.draw(self.screen)



