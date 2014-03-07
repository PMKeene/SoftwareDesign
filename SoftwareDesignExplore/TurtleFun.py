# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 03:25:05 2014

@author: maire
"""
from random import *
from swampy.TurtleWorld import *

world=TurtleWorld()
bob=Turtle()
bob.heading=90

def my_square(x,y,sl):
   bob.x=x
   bob.y=y
   bob.heading=90
   bob.delay=.01
   for i in range(4):   
       fd(bob,sl)
       rt(bob,90)
       
def my_regular_polygon(x,y,sl,s):
   bob.x=x
   bob.y=y
   bob.heading=90
   bob.delay=.01
   for i in range(s):   
       fd(bob,sl)
       rt(bob,360.0/s)
       
    
def my_square2(x,y,sl):
   my_regular_polygon(x,y,sl,4)

def my_circle(x,y,r):
    s=100
    sl=2*pi*r/s
    my_regular_polygon(x-r,y,sl,s)
    
def snow_flake_side(turtle,sl,level):
    """Draw a side of the snowflake curve with a side length of 1 and a recursion depth of level"""
    bob.delay=.001
    if level==1:
        fd(turtle,sl)
        rt(turtle,60)
        fd(turtle,sl)
        lt(turtle,120)
        fd(turtle,sl)
        rt(turtle,60)
        fd(turtle,sl)
    else:
        snow_flake_side(bob,sl/3.0,level-1)
        rt(turtle,60)
        snow_flake_side(bob,sl/3.0,level-1)
        lt(turtle,120)
        snow_flake_side(bob,sl/3.0,level-1)
        rt(turtle,60)
        snow_flake_side(bob,sl/3.0,level-1)
        
def snow_flake(x,y,s,turtle,sl,level):
    bob.x=x
    bob.y=y
    bob.heading=0
    for i in range(s):
        snow_flake_side(turtle,sl,level)
        rt(turtle,360.0/s)
     
def recursive_tree(turtle, branch_length, level):
    """Draw a tree with branch length of branch_length and recursion depth of level"""    
    turtle.delay=.001
    if level==0:
        turtle.pen_color='green'
        fd(turtle, branch_length)
        turtle.undraw()
    else:
        turtle.pen_color='brown'
        fd(turtle, branch_length)
        newTurtle=Turtle()
        newTurtle.x=turtle.x
        newTurtle.y=turtle.y
        newTurtle.heading=turtle.heading
        newTurtle.delay=.001
        lt(newTurtle, random_integers(25,35,1))
        recursive_tree(newTurtle,(uniform(.55,.66,1))*branch_length,level-1)
        newTurtle.undraw()
        bk(turtle,branch_length/3.0)
        newTurtle2=Turtle()
        newTurtle2.x=turtle.x
        newTurtle2.y=turtle.y
        newTurtle2.heading=turtle.heading
        newTurtle2.delay=.001
        rt(newTurtle2, (random_integers(35,45,1)))
        recursive_tree(newTurtle2,(uniform(.6,.69,1)*branch_length,level-1)
        newTurtle2.undraw()
        #bk(turtle,branch_length/6.0)
        #newTurtle3=Turtle()
        #newTurtle3.x=turtle.x
        #newTurtle3.y=turtle.y
        #newTurtle3.heading=turtle.heading
        #newTurtle3.delay=.001
        #lt(newTurtle3, random_integers(40,50,1))
        #recursive_tree(newTurtle3,(uniform(.65,.75,1))*branch_length,level-1)
        #newTurtle3.undraw()
        

if __name__ == "__main__":
    recursive_tree(bob, 90, 5)
    wait_for_user()