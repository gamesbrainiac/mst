'''
Created on Jul 27, 2012

@author: kan
'''
import numpy.random as rd
import matplotlib.pyplot as pp
import numpy

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance2(self, p):
        return (self.x - p.x) ** 2 + (self.y - p.y) ** 2
    def plot(self, marker):
        pp.plot(self.x, self.y, marker)
    
def point_generator(n = 10, bound = 5.0):
    plist = []
    for i in range(n):
        plist.append(point(rd.ranf() * bound, rd.ranf() * bound))
    return plist

def mst(plist):
    connected = [0]
    noconnected = list(range(1, len(plist)))
    edges = []
    while len(connected) < len(plist):
        edge = 0,noconnected[0]
        shortest = plist[0].distance2(plist[noconnected[0]])
        for i in connected:
            for j in noconnected:
                l = plist[i].distance2(plist[j])
                if l < shortest:
                    shortest = l
                    edge = i, j
        connected.append(edge[1])
        noconnected.remove(edge[1])
        edges.append(edge)
    return edges  

def draw_mst(pl, edges):
    pp.figure()
    #pp.subplot(1,3,1)
    for point in pl:
        point.plot('ro')
    for x,y in edges:
        xs = [pl[x].x, pl[y].x]
        ys = [pl[x].y, pl[y].y]
        pp.plot(xs, ys, 'y-', alpha = 1)
    pp.show()
        
def main():
    pl = point_generator(20)
    edges = mst(pl)
    draw_mst(pl, edges)
    
main()
        