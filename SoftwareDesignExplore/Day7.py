# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:58:51 2014

@author: maire
"""

def is_palindrome(string):
    string2=string[::-1]
    if string==string2:
        return True
    else:
        return False

def factorial(n):
    if n==0:
        return 1
    return factorial(n-1)*n
    
def fibonacci(n):
    """ returns the nth value in the fibonacci sequence.
    note that the Oth term of the fibbonaci sequence does not exist, but will return 1
    """
    if n<=2:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)
    
def is_palindrome_recursive(string):
     i=0
     return is_palindrome_recursive(string[i:-i]) and (string[i]==string[-i])
    
if __name__ == "__main__": 
    print fibonacci(6)