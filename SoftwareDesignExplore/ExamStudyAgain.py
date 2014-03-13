# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 20:08:25 2014

@author: maire
"""

def flatten(List):
    Flattened=[]
    for item in List:
        if type(item)==list:
            for subitem in item:
                Flattened.append(subitem)
        else:
            Flattened.append(item)
    return Flattened

def recursive_flatten(List):
    Flattened=[]
    for item in List:
        if type(item)==list:
            Flattened += recursive_flatten(item)
        else:
            Flattened.append(item)
    return Flattened
    
def double_letters(filename):
    f = open(filename,'r')
    fulltext = f.read()
    f.close()
    words=fulltext.split()
    only_doubles={}
    for word in words:
        if is_double(word):
            only_doubles[word]=len(word)
    return only_doubles
    
def is_double(string):
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            return True
    return False

if __name__ == '__main__':
#    print double_letters("words.txt")
#    print flatten([1,2,3])
#    print flatten([1,[2,5],3])
#    print flatten([1,[2,[4,5]],3])
#    print recursive_flatten([1,2,3])
#    print recursive_flatten([1,[2,5],3])
#    print recursive_flatten([1,[2,[4,5]],3])