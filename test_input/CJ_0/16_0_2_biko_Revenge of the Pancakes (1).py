
# coding: utf-8

# In[1]:

import itertools
import io
import networkx as nx
from concurrent.futures import ThreadPoolExecutor
from collections import deque, defaultdict


# In[2]:

TEST_INPUT = """5
-
-+
+-
+++
--+-"""


# In[3]:

SMALL_INPUT = """100
-
-+
+-
+++
--+-
+++-+++-++
--+---+++-
---++-
+-+++--+-+
--+++
+++++
--+--
-+-+-+-+-+
+-+++-++++
-+-+-++---
+++-+---++
---+++-+--
-++-+--+-+
--+-++++-+
-+-++-++--
-+++++----
++
+-++++++--
-+--
+-++
++++-+--
-----
-++----+++
++--
+-+-
---+
-+-+-++++
+++---+-++
+---
+-++---+-+
+-+
--
-+--++-++
--+++-
++---++-++
+---+--
+-+--++---
++--++-++
-+--+-+++-
---+-++-++
-+++
++-++-++-
--+++---+-
--++-+--++
-+---+-+++
++-
--+--++
+--+
-+-+
+--------+
+--+++--++
++--+-
-+-++++++-
+-+-+-+-+-
+-+---+-+-
-++++++++-
+---+
-++---+
-++-
--+++-----
-++--+
---
+
++-+-+----
+++++--+--
++++++++
+++-
--+-+++-+-
-++----+--
---++++---
-+-+---+++
-+---++-
---+++++--
--++
++-+
-++
+--++-++-+
+-+---+++-
++-++-----
------+--
+-------++
++-+-+--++
++-+----+
++++-++-++
++-+---+--
++++
-+-++-+---
+--
-+--+++-+-
-+-
----
+----++--+
---+--+---
--+
--++--++--"""


# In[4]:

SMALL_INPUT1 = """100
-
-+
+-
+++
--+-
++--+++-+-
+---++--+-
--+--++
+-++++++++
-++-+-+-+-
-+-++-----
--+
++---+++-
-+++-++--+
++-+
++-+++--++
--++
++-++-++-+
++
-+-+-+--++
+
--++--+-+-
-+++-+-++-
-+-+
-----
----+-++++
+--+
--
-+-
--+--+++-+
+++-
+-+--+
+-++
+---
-+++
+-+-+-++++
---+-+++++
+--++++--+
---
-++--++
+-+---
--+---+--+
-----+----
+---+++
++--+++++-
-++++++++-
+-++---++-
+-++++++-+
----+
++--++-+--
-+-++++-+-
-+-+++-+-+
-+----
+++-++-+-
-++++-+---
+-+-++--+-
-++--
+-+++-+--+
-++-++++-+
++---+-+-+
+-+--+---+
++-----+-+
++--++++-+
-++-
++-
+---+-+-++
+-+
++----+++
---+--++-+
+---+-
--++-++---
+++++
--++--+++-
--++-
+-+-+-+-+-
+-++-++--+
-+--
-+-+-+++--
-+-+-+-+-+
-++-++-+
----
+--
--+++++-+
+--------+
-+++++++--
-++
---+
++------+-
+-+-
--+-++--++
-+---
-+++-++++-
++++
---+++++--
++--
++-++--+-+
++--++++
+-++-+-+++
++++++-+--
++---++---"""


# In[5]:

def get_cases(data):
    with io.StringIO(data) as stream:
        num_cases = int(stream.readline())
        yield from (line.strip() for line in stream)


# In[6]:

def flip(pile):
    return "".join(map(lambda x: "+" if x == "-" else "-",
                       reversed(pile)))


# In[7]:

def all_flips(pile):
    for i in range(1, len(pile) + 1):
        yield flip(pile[:i]) + pile[i:]


# In[8]:

def is_happy(pile):
    for element in map(lambda x: x == "+",
                       pile):
        if not element:
            return False
    return True


# In[9]:

def find_happiness(pile):
    stack = deque()
    stack.append((pile, 0))
    
    memo = {}
    
    found = -1
    
    while len(stack) != 0:
        current_pile, current_depth = stack.pop()
        if current_pile in memo and memo[current_pile] <= current_depth:
            continue
        if found != -1 and current_depth >= found:
            continue
        memo[current_pile] = current_depth
        
        if is_happy(current_pile):
            found = current_depth
            continue
            
        stack.extend(map(lambda x: (x, current_depth + 1),
                         all_flips(current_pile)))
        
    return found


# In[10]:

def unprocessed(graph):
    return [node
            for node in graph.nodes_iter()
            if graph.out_degree(node) == 0 and not is_happy(node)]


# In[11]:

def find_happiness2(pile):
    graph = nx.DiGraph()
    graph.add_node(pile)
    
    while True:
        count = 0
        
        for node in unprocessed(graph):
            for f in all_flips(node):
                graph.add_path((node, f))
            count += 1
            
        if count == 0:
            break
            
    return nx.shortest_path_length(graph, pile, len(pile) * "+")


# In[12]:

def solve_case(case):
    return find_happiness2(case)


# In[13]:

for index, solution in enumerate(map(solve_case, get_cases(SMALL_INPUT1)), start=1):
    print("Case #{}: {}".format(index, solution))

