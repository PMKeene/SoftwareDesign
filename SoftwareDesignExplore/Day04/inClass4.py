# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/maire/.spyder2/.temp.py
"""
#from math import *
#
#def double(n):
#    return 2*n
#    
#def mtsqrt(n):
#    return sqrt(n)

def get_complementary_base(b):
    """Returns the complementary base nucleotide 
    b: the base represented as a length 1 string
    returns: complementary base represented as a length 1 string"""
    if b=='a':
        return 't'
    elif b=='t':
        return 'a'
    elif b=='c':
        return 'g'
    elif b=='g':
        return 'c'
    else:
        print 'ERROR: Check String Input'
    
def is_between(x,y,z):
    if y<=z and y>=x:
        return True
    else:
        return False
        
#import random

#def random_float(start,stop):
    #random.random(start,stop)

def factorial(n):
    if n==0:
        print 'wtf?'
        return 1
    else:
     s=1
     for i in range(1,n+1):
        s=s*(i)
     return s
        