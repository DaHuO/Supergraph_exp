def solve(S):
    S = list(S)
    count = 0
    for i in range(len(S) - 1, -1, -1):
        if S[i] == '-':
            count += 1
            for j in range(i + 1):
                if S[j] == '-':
                    S[j] = '+'
                else:
                    S[j] = '-'
    return count


T = input()
for i in range(T):
    print 'Case #' + str(i+1) + ': ' + str(solve(raw_input()))
