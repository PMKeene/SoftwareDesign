# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:35:17 2014

@author: maire
"""

#d={'my':1,'secret':2,'code':3}
#also=dict()
#print d['my'],d['secret'],d['code']
#print also
#print d

def histogram(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def reverse_lookup(d,v):
    KeyRing=[]    
    for k in d:
        if d[k]==v:
            KeyRing.append(k)
    return KeyRing
        
def recursive_flatten(List):
    if len([List])==1:
        return List[0]
    else:
        for i in range(len([List])):
            for j in range(len([List[i]])):
                List[i+j]=recursive_flatten(List[i])           
        return List
#        Flattened=[]
#        for i in range(len(List)):
#           for j in range(len([List[i]])):
#               Flattened.append(List[i][j])
#        return Flattened


if __name__ == "__main__":
#   h=histogram('PatriciaMichelleMaireAoifeIsoldePenningtonKeene')
#   k=reverse_lookup(h,1)
#   print k
    print recursive_flatten([1,2,[3,5,[4,6]]])