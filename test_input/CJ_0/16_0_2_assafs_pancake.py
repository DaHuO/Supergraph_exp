#/usr/bin/env python3

def flip_stack(stack):
    flips = 0
    curr = stack.pop(0)

    while len(stack) > 0:
        prev = curr
        curr = stack.pop(0)
        if curr != prev:
            flips += 1

    if curr == '-': flips += 1
    return flips

def solve_case(case):
    stack = list(input())

    result = flip_stack(stack)

    print("Case #{0}: {1}".format(case, result))


def main():
    cases = int(input())
    [solve_case(i+1) for i in range(cases)]

if __name__ == '__main__':
    main()

