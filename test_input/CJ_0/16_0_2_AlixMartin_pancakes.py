FILENAME = 'test.in'
OUTPUT = FILENAME.replace('.in', '.out')

def main():
    with open(OUTPUT, 'w') as g:
        with open(FILENAME) as input:
            T = int(input.readline())
            for t in range(T):
                S = input.readline().strip()
                answer = simple(S)
                answer_str = 'Case #{}: '.format(t+1) + str(answer)
                print(answer_str, S)
                g.write(answer_str)
                g.write('\n')


def reverse_stack(S):
    """
    >>> reverse_stack('--+')
    '-++'
    """
    r = ''
    for ch in S:
        if ch == '+':
            r = '-' + r
        else:
            r = '+' + r
    return r


def successors(new_stack):
    r = []
    for pancakes_flipped in range(1, len(new_stack) + 1):
        new_stack_flipped = reverse_stack(new_stack[:pancakes_flipped]) + new_stack[pancakes_flipped:]
        r.append(new_stack_flipped)
    return r



def simple(s):
    if '-' not in s:
        return 0
    if s[0] == '-':
        if '+' not in s:
            return 1
        first_plus = s.index('+')
        s2 = ''.join(['+'] * first_plus) + s[first_plus:]
        return 1 + simple(s2)
    else:
        first_minus = s.index('-')
        s2 = ''.join(['-'] * first_minus) + s[first_minus:]
        return 1 + simple(s2)


def dpcalc(s):
    S = len(s)
    good_stack = ''.join(['+'] * S)
    r = 0
    reached = set([good_stack])
    frontier = set([good_stack])
    while True:
        if s in reached:
            return r
        r += 1
        newfrontier = set()
        for state in frontier:
            for newstate in set(successors(state)) - reached:
                newfrontier.add(newstate)

        frontier = newfrontier
        reached = reached.union(newfrontier)


if __name__ == '__main__':
    #print(successors('+-+-+++--+'))
    #print(dpcalc('+-+-+++--+'))
    #print(dpcalc('+-+-+++--'))
    main()