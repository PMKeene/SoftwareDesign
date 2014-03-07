# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:22:56 2014

@author: maire
"""
def has_duplicates(list):    
    for i in list:
        for k in range(i+1,len(list)):
            if list[i]==list[k]:
                return True
    return False       
