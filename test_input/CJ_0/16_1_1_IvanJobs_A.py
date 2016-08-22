in_file = 'A-large.in'
out_file = 'A-small-attempt0.out'


def solve(fin, fout):
    T = int(fin.readline().strip())
    for _t in range(1, T + 1):
        S = list(fin.readline().strip())
        N = len(S)
        C = [S[0],]
        for i in range(1, N):
            if S[i] >= C[0]:
                C.insert(0, S[i])
            else:
                C.append(S[i])
        fout.write('Case #%d: %s\n' % (_t, ''.join(C)))



with open(in_file, 'r') as fin, open(out_file, 'w') as fout:
    solve(fin, fout)