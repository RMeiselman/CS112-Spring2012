# Point Object
# =====================================
# Create a Point point class.  Point objects, when created, look like this:
#     >>> pt = Point(3,4)
#     >>> print pt.x
#     3
#     >>> print pt.y
#     4
#
# In addition points have the following methods:
#    distance(self, other):
#        calculates the distance between this point and another
#    
#    move(self, x, y):
#        sets the points location to x,y
# 
#    translate(self, x, y):
#        offsets the point by x and y
# 
#    When all done, points should work like this:
#
#    >>> a = Point(0,0)
#    >>> b = Point(0,0)
#    >>> b.move(2, 2)
#    >>> print b.x, b.y
#    2 2
#    >>> b.translate(1,2)
#    >>> print b.x, b.y
#    3 4
#    >>> print a.distance(b)
#    5

#!/usr/bin/env python
import math

class Point(object):
    #Initializes code
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #Allows you to calculate the distance between two points
    def distance(self, other):
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance
    #Sets the point's location to x,y
    def move(self, x, y):
        self.x = self.x = x
        self.y = self.y = y
    #Offsets the point by x and y
    def translate(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
#Defines the two points, and prints them
a = Point(1,1)
b = Point(2,1)
print a.x, a.y
print b.x, b.y
#Prints the distance between the two points - a & b
print a.distance(b)
#Moves points a & b to the specified points, and prints the new location of the points.
a.move(2,2)
b.move(1,1)
print a.x, a.y
print b.x, b.y
#Offsets the points by x and y, and prints the new location of the points.
a.translate(6,6)
b.translate(5,5)
print a.x, a.y
print b.x, b.y

