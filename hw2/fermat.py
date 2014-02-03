# -*- coding: utf-8 -*-
"""
Think Python Exercise 5-3

@author: maire
"""
def check_fermat(a,b,c,n):
    if a**n+b**n==c**n:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "Nope, that doesn't work."
        
def Fermat():
    a=raw_input('--> ')
    a=int(a)
    b=raw_input('--> ')
    b=int(b)
    c=raw_input('--> ')
    c=int(c)
    n=raw_input('--> ')
    n=int(n)
    check_fermat(a,b,c,n)
    
Fermat()