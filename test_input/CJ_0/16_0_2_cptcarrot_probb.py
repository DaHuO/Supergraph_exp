import queue

def flip(stack, i):
    to_flip = stack[:i]
    to_flip = to_flip.replace('-', '.')
    to_flip = to_flip.replace('+', '-')
    to_flip = to_flip.replace('.', '+')
    stack = to_flip[::-1] + stack[i:]
    return stack

def BFS(start):
    seen = set()
    ref = '+'*len(start)
    Q = queue.Queue()
    Q.put((start, -1, 0))
    seen.add(start)
    while not Q.empty():
        curr = Q.get()
        for i in range(len(curr[0])):
            if i != curr[1]:
                new = flip(curr[0], i+1)
                if new == ref:
                    return curr[2]+1
                if new not in seen:
                    Q.put((new, i, curr[2]+1))
                    seen.add(Q)
    return None

def solve_v2(pancakes):
    if pancakes[-1] == '+':
        i = pancakes.rfind('-')
        if i == -1:
            return 0
        return solve_v2(pancakes[:i+1])
    else: # pancakes[-1] == '-'
        i = pancakes.find('-')
        if i == 0:
            i = len(pancakes)
        return 1 + solve_v2(flip(pancakes, i))
        
        
def solve():
    infile = open('B-large.in')
    outfile = open('B-large.out', 'w')
    N = int(infile.readline().strip())
    for i in range(N):
        stack = infile.readline().strip()
        res = "Case #%d: %s\n" % (i+1, solve_v2(stack))
        outfile.write(res)
    infile.close()
    outfile.close()

solve()
