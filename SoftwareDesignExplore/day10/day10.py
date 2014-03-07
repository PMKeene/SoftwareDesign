# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:30:03 2014

@author: maire
"""

def get_words_from_book(file):
    f=open('/home/maire/SoftwareDesignLocal/day10/'+file,'r')    
    L=f.read()
    f.close()
    start=L.index(" ***")
    end=L.index("End of Project Gutenberg")
    L=L[start+4:end-1]
    
    list_of_strings=L.split()
    print list_of_strings
    
if __name__ == "__main__": 
    get_words_from_book("159.txt")