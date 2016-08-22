import sys


def flip_pancake(p):
    if p == '+': return '-'
    if p == '-': return '+'


def flip(n, stack):
    top = stack[0:n]
    bottom = stack[n:]
    top.reverse()

    top = [(flip_pancake(x[0]), x[1]) for x in top]

    if len(bottom) == 0:
        return top

    if top[n - 1][0] == bottom[0][0]:
        return top[:-1] + [(top[n - 1][0], top[n-1][1] + bottom[0][1])] + bottom[1:]

    return top + bottom


def flipped_stacks(stack):
    for i in range(len(stack)):
        yield flip(i + 1, stack)


def smallest_stack(stack):
    min = len(stack)
    ret = stack

    for s in flipped_stacks(stack):
        if len(s) < min:
            ret = s

    return ret


def solution(case):
    stack = case
    count = 0

    while len(stack) > 1:
        stack = smallest_stack(stack)
        count += 1

    if stack[0][0] == '-':
        count += 1

    return count


def parse_case(raw_case):
    cur_sign = raw_case[0]
    cur_count = 1
    ret = []

    for i, c in enumerate(raw_case[1:]):
        if c == cur_sign:
            cur_count += 1
        else:
            ret.append((cur_sign, cur_count))
            cur_sign = raw_case[i + 1]
            cur_count = 1

    ret.append((cur_sign, cur_count))

    return ret

def test_cases(path):
    for i, l in enumerate(open(path)):
        if i > 0:
            yield i, parse_case(l.strip())

if __name__ == '__main__':
    for case in test_cases(sys.argv[1]):
        print('Case #{}: {}'.format(case[0], solution(case[1])))
