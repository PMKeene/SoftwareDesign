# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/maire/.spyder2/.temp.py
"""

def exclusive_or_dict(d1,d2):
    exclusive_dict={}    
    for key in d1:
         if (key in d2)==False:
             exclusive_dict[key]= d1[key]
             
    for key in d2:
        if (key in d1)==False:
            exclusive_dict[key]= d2[key]
        
    return exclusive_dict
    

if __name__ == '__main__':
   print exclusive_or_dict({'a':5,'b':3},{'a':7,'c':3})
   print exclusive_or_dict({'test':5,'b':7.0, 3:'q',},{'b':'world',3:'q'})