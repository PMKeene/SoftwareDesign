# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 14:09:03 2014

@author: maire
"""
from math import sqrt

class Point(object):
    """Represents a point in 2-D space."""


def print_point(p):
    """Print a Point object in human-readable format."""
    print '(%g, %g)' % (p.x, p.y)


class Rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


def find_center(rect):
    """Returns a Point at the center of a Rectangle."""
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modify the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight 
    
    
    
def distance_between_points(Point1,Point2):
    return (sqrt((Point2.x-Point1.x)**2 + (Point2.y-Point1.y)**2))
    
def move_rectangle(Rectangle,dx,dy):
    Rectangle.corner.x += dx
    Rectangle.corner.y += dy

def move_rectangle_conserve(Rectangle,dx,dy):
    new_Rectangle=Rectangle()
    new_Rectangle.corner.x=Rectangle.corner.x+dx
    new_Rectangle.corner.y=Rectangle.corner.y+dy
    
if __name__ == '__main__':
    Here=Point()
    There=Point()
    
    Here.x=8
    Here.y=4
    
    There.x=3
    There.y=4
    
    print distance_between_points(Here, There)
    
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0