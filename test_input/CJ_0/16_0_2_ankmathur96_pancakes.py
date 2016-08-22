def count_inversions(s):
    current = s[0]
    inversions = 0
    for i in range(1,len(s)):
        if current != s[i]:
            inversions += 1
            current = s[i]
    if s[-1] == '-':
        inversions += 1
    return inversions

def greedy_inversions(s):
    print(s, len(s), '+' * len(s))
    if s == '+' * len(s):
        return 0
    else:
        n_flips = count_inversions(s)
        print(n_flips)
        return n_flips

if __name__ == '__main__':
    f_stub = 'B-large'
    f = open(f_stub + '.in', 'r')
    o = open(f_stub + '.out', 'w')
    n_cases = int(f.readline().strip())
    i = 0
    while i < n_cases:
        pancake_str = f.readline().strip()
        n_flips = greedy_inversions(pancake_str)
        i += 1
        o.write('Case #' + str(i) + ': ' + str(n_flips) + '\n')
    f.close()
    o.close()
