

def solution(stack):
    flips = 0
    c_last = None
    for c in stack:
        if c_last is None:
            c_last = c
            continue
        if c_last != c:
            flips += 1
            c_last = c

    if c_last != '+':
        flips += 1

    return flips


def main():
    with open('p2.in', 'r') as f:
        lines = f.readlines()

    t = lines.pop(0)
    for i, line in enumerate(lines):
        stack = line.strip()
        flips = solution(stack)
        print 'Case #{}: {}'.format(i+1, flips)



if __name__ == '__main__':
    main()
