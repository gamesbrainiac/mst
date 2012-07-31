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
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5
    def plot(self, marker):
        pp.plot(self.x, self.y, marker)
    def pair_dis2(self, pr):
        if self.distance2(pr.ps[0]) < self.distance2(pr.ps[1]):
            edge = self, pr.ps[0]
            return self.distance2(pr.ps[0]), edge
        else:
            edge = self, pr.ps[1]
            return self.distance2(pr.ps[1]), edge

class pair:
    def __init__(self, lp, rp):
        self.ps = [lp, rp]
    def dis2(self, pair2):
        buffer = float('inf')
        for p1 in self.ps:
            for p2 in pair2.ps:
                if p1.distance2(p2) < buffer:
                    buffer = p1.distance2(p2)
                    twoend = p1, p2
        return buffer,twoend
    def plot(self, m1, m2):
        lp, rp = self.ps
        lp.plot(m1)
        rp.plot(m2)
    
def point_generator(n = 10, bound = 5.0):
    plist = []
    for i in range(n):
        plist.append(point(rd.ranf() * bound, rd.ranf() * bound))
    return plist

def prim(pl):
    connected = [0]
    dis = list(range(1, len(pl)))
    edges = []
    sum = 0
    while len(connected) < len(pl):
        shortest = float('inf')
        for i in connected:
            for j in dis:
                l = pl[i].distance2(pl[j])
                if l < shortest:
                    shortest = l
                    edge = pl[i],pl[j]
                    idx = i,j
        sum += shortest
        connected.append(idx[1])
        dis.remove(idx[1])
        edges.append(edge)
    return edges, sum

def draw_prim(pl, edges):
    pp.figure()
    #pp.subplot(1,3,1)
    for point in pl:
        point.plot('ro')
    for p,q in edges:
        xs = [p.x, q.x]
        ys = [p.y, q.y]
        pp.plot(xs, ys, 'y-', alpha = 1)
    pp.show()


def pair_generator(n = 10, bound = 10.0):
    pl = point_generator(n, bound)
    pairlist = [pair(p, point((p.x + 1.0), p.y)) for p in pl]
    return pairlist
    
def pair_prim(pl):
    b = float('inf')
    for i in range(len(pl)):
        for j in range(len(pl)):
            if i != j:
                dis, twoend = pl[i].dis2(pl[j])
                if dis < b:
                    b = dis
                    edge = twoend
                    connected = [i, j]
    sum = b
    edges = [edge]
    tree = list(edge)
    dis = list(range(len(pl)))
    dis.remove(connected[0])
    dis.remove(connected[1])
    
    while len(connected) < len(pl):
        b = float('inf')
        for p in tree:
            for pridx in dis:
                l, edge = p.pair_dis2(pl[pridx])
                if l < b:
                    b = l
                    opt_edge = edge
                    opt_idx = pridx
        sum += b
        tree.append(opt_edge[1])
        edges.append(opt_edge)
        dis.remove(opt_idx)
        connected.append(opt_idx)
    return edges, sum


def draw_pair_prim(prl, edges, opt_e):
    pp.figure()
    for pr in prl:
        pr.plot('ro', 'bx')
    for e in edges:
        p, q = e
        xs = [p.x, q.x]
        ys = [p.y, q.y]
        pp.plot(xs, ys, 'y-', alpha = 1)
    for e in opt_e:
        p, q = e
        xs = [p.x, q.x]
        ys = [p.y, q.y]
        pp.plot(xs, ys, 'b-', alpha = 1)       
    pp.show()

def brute_opt_prim(prl):
    opt_sum = float('inf')
    for i in range(2 ** len(prl) - 1):
        key = str(bin(i))[2:]
        key = '0'*(len(prl) - len(key)) + key
        pl = []
        for j in range(len(prl)):
            pl.append(prl[j].ps[int(key[j])])
        edges, sum = prim(pl)
        if sum < opt_sum:
            opt_edges, opt_sum = edges, sum
    return opt_edges, opt_sum
                        
def main_prim():
    pl = point_generator(20)
    edges, sum = prim(pl)
    draw_prim(pl, edges)
    
def main_pair(np):
    prl = pair_generator(np)
    edges, sum = pair_prim(prl)
    opt_edges, sum2 = brute_opt_prim(prl)
    draw_pair_prim(prl, edges, opt_edges)
    
#def main_opt(n):
#    prl = pair_generator(n)
#    edges, sum1 = pair_prim(prl)
#    opt_edges, sum2 = brute_opt_prim(prl)
#    return sum1/sum2
#def opt_test(n, np):
#    worst = 0
#    for i in range(n):
#        ratio = main_opt(np)
#        if ratio > worst:
#            worst = ratio
#    print(worst)

main_pair(15)
    
 
        