from functools import lru_cache
from queue import Queue

N = int(input())

def flip(word, k):
    return ''.join(reversed(word[:k])).replace('-', '0').replace('+', '-').replace('0', '+') + word[k:]

def solve(word):
    q = Queue()
    visited = set()
    distances = {}
    distances[word] = 0
    visited.add(word)
    q.put(word)
    while not q.empty():
        item = q.get()

        if '-' not in item:
            return distances[item]

        neighbors = [flip(item, k) for k in range(1, len(word) + 1)]
        for neigh in neighbors:
            if neigh not in visited:
                visited.add(neigh)
                distances[neigh] = distances[item] + 1
                q.put(neigh)                

for I in range(1, N+1):
    result = solve(input())

    print("Case #%d: %d" % (I, result))
