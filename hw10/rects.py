#!/usr/bin/env python
"""
rects.py

Pygame Rectangles
=========================================================
The following section will test your knowledge of how to 
use pygame Rect, arguably pygame's best feature. Define
the following functions and test to make sure they 
work with `python run_tests.py`

Make sure to use the documentation 
http://www.pygame.org/docs/ref/rect.html


Terms:
---------------------------------------------------------
  Point:     an x,y value
               ex:  pt = 3,4

  Polygon:   a shape defined by a list of points
               ex:  poly = [ (1,2), (4,8), (0,3) ]

  Rectangle:  pygame.Rect
"""

# 1. poly_in_rect
#      Check to see if the polygon is completely within a given 
#      rectangle.
#
#      returns:  True or False

import pygame
from pygame.locals import *

## For some reason the "rect.collidelist" we used in class didn't work, so I tried "collidepoint" instead.

def poly_in_rect(poly, rect):
    "check if polygon is within rectangle"
    
    for point in poly:
       if rect.collidepoint(point) != 1:
           return True
       else:
           return False
    

# 2. surround_poly
#      Create a rectangle which contains the given polygon.  
#      It should return the smallest possible rectangle 
#      where poly_in_rect returns True.
#
#      returns:  pygame.Rect

## I tried to use the "Rect.fit" from the documentation (because it seemed like it did exactly what this prblem needed) but it didn't work. So here's a much more long winded version.

# None of the "pythonic" ways I found for doing any of these problems have worked so far and it makes me :(

def surround_poly(poly):
    "create a rectangle which surounds a polygon"

    xmin, ymin = xmax, ymax = poly[0]
    
    if poly_in_rect == True:

        for point in poly:
            x, y = point
            if x <= xmin:
                xmin = x
            if x >= xmax:
                xmax = x
            if y <= ymin:
                ymin = y
            if y >= ymax:
                ymax = y

    return Rect(xmin, ymin, (xmax - xmin + 1), (ymax - ymin + 1))

        
        

