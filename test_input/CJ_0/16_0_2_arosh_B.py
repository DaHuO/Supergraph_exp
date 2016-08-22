# coding: UTF-8

def flip(S):
    return S.translate(str.maketrans('+-', '-+'))[::-1]

def solve(S):
    c = 0
    while True:
        if '-' not in S:
            break
        en = len(S)
        while True:
            assert en - 1 >= 0
            if S[en - 1] == '+':
                en -= 1
            else:
                break
        st = 0
        while True:
            assert st < len(S)
            if S[st] == '+' and st + 1 < len(S):
                st += 1
            else:
                break
        # print('st = {}, en = {}'.format(st, en))
        if st > 0:
            S = flip(S[:st]) + S[st:]
            c += 1
            # print('S = {}'.format(S))
        if '-' not in S:
            break
        S = flip(S[:en]) + S[en:]
        # print('S = {}'.format(S))
        c += 1
        if '-' not in S:
            break
    return c

def main():
    T = int(input())
    for i in range(T):
        S = input()
        print('Case #{}: {}'.format(i + 1, solve(S)))

if __name__ == '__main__':
    main()
