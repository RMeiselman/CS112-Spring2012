#!/usr/bin/python env

def point_in_box(pt, box):
    x1,y1 = pt
    x2,y2,w,h = box
    return y1 >= y2 and y1 < y2 + h and x1 >= x2 and x1 < x2 + w

# Calculate if a point is within a box
#    check if a point is inside a given box.  
#
#    Parameters:
#       pt: list of 2 numbers (x,y)
#       box: list of 4 numbers (x,y,w,h).  x,y is the top left point.  w,h is the width and height

# def point_in_box(pt, box):





