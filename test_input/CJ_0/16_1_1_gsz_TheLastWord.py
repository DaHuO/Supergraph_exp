#!/usr/bin/env python3

def solve_case(S):
    revfront = [S[0]]
    back = []
    for c in S[1:]:
        if c >= revfront[-1]:
            revfront.append(c)
        else:
            back.append(c)
    revfront.reverse()
    return ''.join(revfront + back)

def main():
    T = int(input())
    for ci in range(1, T+1):
        print('Case #{}: {}'.format(ci, solve_case(input())))

if __name__ == '__main__':
    main()

