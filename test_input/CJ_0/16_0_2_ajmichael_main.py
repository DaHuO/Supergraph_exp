import sys

memoized = {}
best_paths = {}

def compute(stack):
    key = "".join(stack)
    if key in best_path and sofar >= best_paths[key]:
        return
    if len(stack) == 0:
        return 0
    if stack[-1] == '+':
        return compute(stack[:-1])

    best_solution = 9999999999999999999999999
    for index in range(1, len(stack)+1):
        newstack = flip(stack, index)
        solution = 1 + compute(newstack, sofar+1)
        if solution < best_solution:
            best_solution = solution
    return best_solution

def compute(stack):
    queue = [(reduce(stack), 0)]
    seen = []
    while len(queue) > 0:
        c_stack, c_val = queue.pop(0)
        if len(c_stack) == 0:
            return c_val
        if c_stack not in seen:
            seen += [c_stack]
            nbs = neighbors(c_stack)
            nvals = [c_val + 1 for x in nbs]
            queue += zip(nbs, nvals)

def reduce(stack):
    if len(stack) == 0:
        return stack
    elif stack[-1] == '+':
        return reduce(stack[:-1])
    else:
        return stack

def neighbors(stack):
    return [reduce(flip(stack, index)) for index in range(1, len(stack) + 1)]

def flip(stack, index):
    top_part = stack[:index]
    bottom_part = stack[index:]
    top_flipped = [swapsign(p) for p in list(reversed(top_part))]
    return top_flipped + bottom_part

def swapsign(sign):
    if sign == '+':
        return '-'
    else:
        return '+'

with open(sys.argv[1], "r") as f:
    skip = True
    i = 1
    for line in f:
        if not skip:
            print 'Case #' + str(i) + ':',
            i = i + 1
            print compute(list(line.strip()))
        else:
            skip = False
