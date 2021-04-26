#!/usr/bin/env python
# coding: utf-8

# In[1]:

class VectorV5:
    '''define the vector'''  # this is the document string
    dim = 2   # this is the attribute
    
    def __init__(self, x=0.0, y=0.0):  # any method in Class requires the first parameter to be self!
        '''initialize the vector by providing x and y coordinate'''
        self.x = x
        self.y = y
        
    def norm(self): 
        '''calculate the norm of vector'''
        return math.sqrt(self.x**2+self.y**2)
    
    def __add__(self, other):
        '''calculate the vector sum of two vectors'''
        return VectorV5(self.x + other.x, self.y + other.y)
    
    def __repr__(self):   #special method of string representation
        '''display the coordinates of the vector'''
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __mul__(self, scalar):
        '''calculate the scalar product'''
        return VectorV5(self.x * scalar, self.y * scalar)

string = 'Python'

def print_hello():
    print("Hello")

