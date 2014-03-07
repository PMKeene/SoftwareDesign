# -*- coding: utf-8 -*-
"""
Spyder Editor

Maire Keene
"""

def sum_of_squares(n):
    squares=[]
    for i in range(1,n+1):
        square=i**2
        squares.append(square)
    return sum(squares)
    
def filter_out_negative_numbers(list):
    Filtered=[]    
    for i in range(len(list)):
        if list[i] >=0:
            Keepers=list[i]
            Filtered.append(Keepers)
    return Filtered