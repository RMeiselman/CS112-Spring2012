#!/usr/bin/env python

import math

#the function ptop measures the distance between one point and another point,
#using 4 numbers inputted by the user
def ptop((x1, y1), (x2, y2)):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

#takes four numbers from the user
x1 = int(raw_input("enter a number for x1: "))
y1 = int(raw_input("enter a number for y1: "))
x2 = int(raw_input("enter a number for x2: "))
y2 = int(raw_input("enter a number for y2: "))
print "the distance between those points is: ",ptop((x1, y1), (x2, y2))









# Distance formula
#   calculate a function called "distance" to calculate the distance between two points.
#   http://www.purplemath.com/modules/distform.htm
#   ex: 
#      >>> distance((0,0), (3,4))
#      5

# def distance(a, b):


