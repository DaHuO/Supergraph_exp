def answer(f):
    moves = 0

    while f != ['+'] * len(f):
        moves += 1
        pos = (len(f) - 1) - f[::-1].index('-')

        for i in range(pos + 1):
            if f[i] == '-':
                f[i] = '+'
            else:
                f[i] = '-'

    return moves

def main():
    t = int(input())
    
    for c in range(t):
        f = list(input())
        print("Case #%d: %d" % (c + 1, answer(f)))

if __name__ == "__main__":
    main()
