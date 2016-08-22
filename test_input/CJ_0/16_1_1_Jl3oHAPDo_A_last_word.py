#!python3

def solve(S):
    start_str = S[0]
    tmp_str = start_str
    for a in S.upper()[1:]:
        if a >= tmp_str[0]:
            tmp_str = a + tmp_str
        else:
            tmp_str = tmp_str + a
    return tmp_str



if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
    for case in range(1, T + 1):
        S = str(f.readline())
        answer = solve(S)
        print("Case #{0}: {1}".format(case, answer), end='')