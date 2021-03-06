#!/usr/bin/env python

import pygame
from resource import load_image

class SpriteSheet(object):
    def __init__(self, image, dimensions, colorkey=-1):       ###colorkey=-1 is to get rid of background color of spritesheet%%%
        if type(image) is str:
            image = load_image(image)
        if colorkey == -1:
            colorkey = image.get_at((0,0))
        if colorkey:
            image.set_colorkey(colorkey)

        cols, rows = dimensions
        w = self.width = 1.0 * image.get_width() / cols
        h = self.height = 1.0 * image.get_height() / rows       ### tells the program how many sprites are in the spritesheet ###

        self._images = []
        for y in range(rows):
            row = []
            for x in range(cols):
                row.append(image.subsurface((x*w, y*h, w, h)))
            self._images.append(row)

    def get(self, x, y):
        return self._images[y][x]


    
        
