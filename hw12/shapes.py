#!/usr/bin/env python

import math

# Shapes
# =========================================================
# 
# Define a shape object.  This object has abstract (empty) 
# methods for calculating the area and perimeter of the 
# shape.
#
# After that, create classes for Rectangles, Squares, 
# and Circles.
# 
# When done, the code should work like this.
#     >>> r = Rect(3,4)
#     >>> print r.area()
#     12
#     >>> sq = Square(5)
#     >>> print sq.perimeter()
#     20
#     >>> print isinstance(sq, Rectangle)
#     True
#     >>> c = Circle(3)
#     >>> print c.area()
#     28.274333882308138
#     


class Shape(object):
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width*2 + self.height*2

class Square(Rect):
    def __init__(self,side):
        Rect.__init__(self, side, side)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius**2) * math.pi

    def perimeter(self):
        return (math.pi*2) * self.radius
