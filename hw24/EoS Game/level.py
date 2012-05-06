#!/usr/bin/env python

import os

import pygame
from pygame import Rect, Surface

class Level(object):
    def __init__(self, size):
        self.bounds = Rect((0,0), size)

    def restart(self):
        self.player = Player()
        self.player.rect.center = self.bounds.center

    def update(self, dt):
        self.player.update(dt)
