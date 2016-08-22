"""
Author: Aadil Ahamed
pancakes.py: Google Code Jam problem 2
"""


def farthest_blank(S):
    index = -1
    for i in range(len(S)):
        if S[i] == '-':
            index = i
    return index


def invert(char):
    if char == '+':
        return '-'
    elif char == '-':
        return '+'
    else:
        print("Error!!!!!!")
        quit()

def flip_stack(S, i):
    top = S[:i+1]
    inverted_top = []
    for i in range(len(top)):
        inverted_top.append(invert(top[i]))
    inverted_top = inverted_top[::-1] # reverse
    return inverted_top + S[i+1:]

def num_top(S):
    i = 0
    while S[i] == '+':
        i += 1
    return i-1

def num_flips(S):
    num = 0
    index = farthest_blank(S)
    while index > -1:
        if S[0] == '+':
            S = flip_stack(S, num_top(S))
            num += 1
        S = flip_stack(S, index)
        index = farthest_blank(S)
        num += 1
    return num


def test_flip():
    S = list("--+-")
    print(flip_stack(S, 3))
    print(flip_stack(S, 1))
    print(flip_stack(S, 0))
    print(num_flips(S))

def test():
    test_flip()

def main():
    #test()
    T = int(input())
    for i in range(T):
        S = list(input())
        print("Case #{}: {}".format( i+1, num_flips(S) ) )


if __name__ == "__main__":
    main()
