def read_data(filename):
    with open(filename) as f:
        cases = int(f.readline().strip())
        for case in xrange(cases):
            stack = f.readline().strip()
            solve(stack, case + 1)

def solve(stack, case):
    steps = 0
    top = 0
    current = stack[0]
    while top < len(stack):
        if stack[top] != current:
            steps += 1
            current = stack[top]
        top += 1

    if not current == '+':
        # Flip all the stack
        steps += 1
    print 'Case #{}: {}'.format(case, steps)

if __name__ == '__main__':
    read_data('B-large.in')
