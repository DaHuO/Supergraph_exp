def compress(s):
    out = [1 if s[0] == '+' else 0]
    for c in s[1:]:
        d = 1 if c == '+' else 0
        if d != out[-1]:
            out.append(d)

    return out

def main():
    T = int(input())
    for case_num in range(1, T + 1):
        s = compress(input())
        moves = 0
        if s[-1] == 1:
            s = s[:-1]

        print("Case #{0}: {1}".format(case_num, len(s)))

if __name__ == '__main__':
    main()
