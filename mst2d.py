'''
Created on Jul 27, 2012

@author: kan
'''
import numpy.random as rd
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance2(self, p):
        return (self.x - p.x) ** 2 + (self.y - p.y)
    
def point_generator(n = 10, bound = 5.0):
    plist = []
    for i in range(n):
        plist.append(point(rd.ranf() * bound, rd.ranf() * bound))
    return plist


        
