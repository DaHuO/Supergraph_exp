from __future__ import print_function, division
import sys
from collections import defaultdict, Hashable
from functools import partial
from random import shuffle, choice
import heapq
from itertools import izip,groupby

class heap:
    def __init__(self, node):
        self.nodes = []
        heapq.heappush(self.nodes, (0, node))
    
    def empty(self):
        return len(self.nodes) == 0
    
    def push(self, node, priority):
        heapq.heappush(self.nodes, (priority, node))
    
    def pop(self):
        return heapq.heappop(self.nodes)[1]

def simplify(p):
    return ''.join(c for c, _ in groupby(p))
    
def flip_pancake(p, pos):
    top, bottom = p[:pos+1], p[pos+1:]
    switch = {'-':'+', '+':'-'}
    
    flipped = [switch[c] for c in top[::-1]]
    
    return simplify(''.join(flipped)+bottom)

def sort_pancake(p):

    goal = '+'
    open_set = heap(p)
    closed_set = set()
    g = defaultdict(lambda: 10**10)
    g[p] = 0
    #f = defaultdict(lambda: 10**10)
    eval_count = 0
    while not open_set.empty():
        cur = open_set.pop()
        eval_count+=1
        if cur == goal:
            break
        closed_set.add(cur)
        
        split_points = range(len(p))
        for point in split_points:
            flipped = flip_pancake(cur, point)
            new_score = g[cur] + 1
            if flipped not in closed_set and new_score < g[flipped]:
                open_set.push(flipped, new_score + len(flipped))
                g[flipped] = new_score
                #print('pushed', flipped, new_score)
    print('evals:', eval_count)
    return g[goal]
        
def read_case(f):
    s = simplify(f.readline().rstrip())
    return s

def print_case(result, n, f):
    text = "Case #%d: %s" % (n,result)
    out.write(text + '\n')
    print(text)
    
def do_case(case):
    p = case
    res = sort_pancake(p)
    print(p, res)
    return res
    
in_ = open(sys.argv[1], 'r')
num_cases = int(in_.readline())
cases = [read_case(in_) for n in range(num_cases)]
#cases = [''.join([choice('-+') for i in range(100)]) for j in range(200)]
results = [do_case(case) for case in cases]

out = open(sys.argv[2], 'w')
for n,result in enumerate(results):
    print_case(result, n+1, out)
