# coding: UTF-8

def solve(S):
    tmp = ''
    for i in range(len(S)):
        head = S[i] + tmp
        tail = tmp + S[i]
        tmp = max(head, tail)
    return tmp

def main():
    T = int(input())
    for case in range(1, T + 1):
        S = input()
        print('Case #{}: {}'.format(case, solve(S)))

if __name__ == '__main__':
    main()
