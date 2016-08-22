if __name__ == '__main__':
    T = int(input())
    for t in range(1,T+1):
        S = input() + '+'
        flips = sum((1 for x,y in zip(S,S[1:]) if x != y))
        print("Case #{}: {}".format(t, flips))
