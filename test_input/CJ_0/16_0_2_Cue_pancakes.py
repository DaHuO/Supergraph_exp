import numpy as np
import sys
sys.setrecursionlimit(100000)

filename = 'B-small-attempt0.in'
out_filename = 'out_data.dat'

out_file = open(out_filename,'w')
with open(filename,'r') as in_file:
    count = int(in_file.readline())
    data = [line.rstrip() for line in in_file]


print count
print data

def flip(stack,i):
    top = stack[0:i+1]
    bottom = stack[i+1:]
    reverse_top = list(reversed(list(top)))
    flipped_top = []
    for cake in reverse_top:
        if cake == '+':
            flipped_top.append('-')
        elif cake == '-':
            flipped_top.append('+')
    flipped_top_str = ''.join(flipped_top)
    flipped_stack = flipped_top_str + bottom
    print "Flipped:" +flipped_stack
    return flipped_stack
    

def happy_stack(stacks_to_check,visited,count_queue):
    '''Breadth first search of a correct flip
    '''
    #try all the flips
    active_stack = stacks_to_check.pop(0)
    active_count = count_queue.pop(0)
    if '-' not in active_stack:
        print 'DONE'
        return active_count 
    if active_stack not in visited:
        visited.add(active_stack)
        for index,_ in enumerate(active_stack):
            flipped_stack = flip(active_stack,index)
            stacks_to_check.append(flipped_stack)
            count_queue.append(active_count +1)
    return happy_stack(stacks_to_check,visited,count_queue)
'''
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited
'''

def write_output(out_file,N_list):
    case_int = 1
    for N in N_list:
        out_file.write('Case #{0}: {1}\n'.format(case_int,N))
        case_int += 1

N_list = []
for stack in data:
    flip_count = happy_stack([stack],set(),[0])
    N_list.append(flip_count)


write_output(out_file,N_list)
out_file.close()
